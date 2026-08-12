#!/usr/bin/env python3

import csv
import math
import sys

import rclpy
from geometry_msgs.msg import Twist
from nav2_msgs.action import NavigateToPose
from nav_msgs.msg import Odometry
from rclpy.action import ActionClient
from rclpy.node import Node

from send_goal import yaw_to_quaternion


class DynamicObstacleTest(Node):
    def __init__(self):
        super().__init__('dynamic_obstacle_test')
        self.declare_parameter('output_file', 'dynamic_obstacle_test.csv')
        self.output_file = self.get_parameter('output_file').value
        self.client = ActionClient(self, NavigateToPose, 'navigate_to_pose')
        self.rows = []
        self.create_subscription(Twist, 'cmd_vel', self.on_cmd_vel, 10)
        self.create_subscription(Odometry, 'odom', self.on_odom, 10)

    def on_cmd_vel(self, msg):
        stamp = msg.header.stamp
        self.rows.append([
            f'{stamp.sec}.{stamp.nanosec:09d}',
            msg.linear.x, msg.linear.y, msg.angular.z,
        ])

    def on_odom(self, msg):
        stamp = msg.header.stamp
        pose = msg.pose.pose
        self.rows.append([
            f'{stamp.sec}.{stamp.nanosec:09d}',
            pose.position.x, pose.position.y, pose.orientation.z,
        ])

    def run(self, x, y, yaw, frame_id='map'):
        if not self.client.wait_for_server(timeout_sec=10.0):
            self.get_logger().error('Nav2 action server not available')
            return False

        goal_msg = NavigateToPose.Goal()
        goal_msg.pose.header.frame_id = frame_id
        goal_msg.pose.header.stamp = self.get_clock().now().to_msg()
        goal_msg.pose.pose.position.x = x
        goal_msg.pose.pose.position.y = y
        qx, qy, qz, qw = yaw_to_quaternion(yaw)
        goal_msg.pose.pose.orientation.x = qx
        goal_msg.pose.pose.orientation.y = qy
        goal_msg.pose.pose.orientation.z = qz
        goal_msg.pose.pose.orientation.w = qw

        self.get_logger().info('Start dynamic obstacle test')
        send_future = self.client.send_goal_async(goal_msg)
        rclpy.spin_until_future_complete(self, send_future)
        goal_handle = send_future.result()
        if not goal_handle.accepted:
            self.get_logger().warn('Goal rejected')
            return False
        result_future = goal_handle.get_result_async()
        rclpy.spin_until_future_complete(self, result_future)
        self.get_logger().info('Goal finished: %s', result_future.result().status)
        self.save()
        return True

    def save(self):
        with open(self.output_file, 'w', newline='') as handle:
            writer = csv.writer(handle)
            writer.writerow([
                'stamp', 'cmd_vx', 'cmd_vy', 'cmd_wz',
                'odom_x', 'odom_y', 'odom_qz',
            ])
            for row in self.rows:
                if len(row) == 4:
                    writer.writerow(row + ['', '', ''])
                else:
                    writer.writerow(['', '', '', ''] + row)
        self.get_logger().info('Saved %d samples to %s', len(self.rows), self.output_file)


def main(args=None):
    rclpy.init(args=args)
    node = DynamicObstacleTest()
    try:
        if len(sys.argv) < 4:
            node.get_logger().error(
                'Usage: dynamic_obstacle_test.py X Y YAW [frame_id]')
            return
        node.run(
            float(sys.argv[1]),
            float(sys.argv[2]),
            float(sys.argv[3]),
            sys.argv[4] if len(sys.argv) > 4 else 'map')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
