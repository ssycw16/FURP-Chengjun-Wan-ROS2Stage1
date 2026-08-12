#!/usr/bin/env python3

import math
import sys

import rclpy
import yaml
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from rclpy.node import Node


class DeadReckoningFollower(Node):
    def __init__(self):
        super().__init__('follow_waypoints_dead_reckoning')
        self.declare_parameter('max_speed', 0.25)
        self.declare_parameter('max_turn_speed', 0.8)
        self.declare_parameter('goal_tolerance', 0.15)
        self.declare_parameter('yaw_tolerance', 0.2)

        self.max_speed = self.get_parameter('max_speed').value
        self.max_turn_speed = self.get_parameter('max_turn_speed').value
        self.goal_tolerance = self.get_parameter('goal_tolerance').value
        self.yaw_tolerance = self.get_parameter('yaw_tolerance').value
        self.latest_odom = None
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        self.create_subscription(Odometry, 'odom', self.on_odom, 10)

    def on_odom(self, msg):
        self.latest_odom = msg

    def current_pose(self):
        pose = self.latest_odom.pose.pose
        yaw = 2.0 * math.atan2(pose.orientation.z, pose.orientation.w)
        return pose.position.x, pose.position.y, yaw

    def normalize_angle(self, angle):
        while angle > math.pi:
            angle -= 2.0 * math.pi
        while angle < -math.pi:
            angle += 2.0 * math.pi
        return angle

    def publish_twist(self, linear, angular):
        msg = Twist()
        msg.linear.x = linear
        msg.angular.z = angular
        self.publisher.publish(msg)

    def move_to(self, target_x, target_y, target_yaw=None):
        rate = self.create_rate(20)
        while rclpy.ok():
            if self.latest_odom is None:
                rate.sleep()
                continue
            x, y, yaw = self.current_pose()
            dx = target_x - x
            dy = target_y - y
            distance = math.hypot(dx, dy)

            if distance < self.goal_tolerance:
                if target_yaw is None:
                    break
                yaw_error = self.normalize_angle(target_yaw - yaw)
                if abs(yaw_error) < self.yaw_tolerance:
                    break
                self.publish_twist(
                    0.0, math.copysign(self.max_turn_speed, yaw_error))
            else:
                desired_yaw = math.atan2(dy, dx)
                yaw_error = self.normalize_angle(desired_yaw - yaw)
                forward_gain = max(0.0, math.cos(yaw_error))
                linear = self.max_speed * forward_gain
                angular = max(
                    -self.max_turn_speed,
                    min(self.max_turn_speed, yaw_error))
                self.publish_twist(linear, angular)
            rate.sleep()
        self.publish_twist(0.0, 0.0)

    def run(self, waypoint_file):
        with open(waypoint_file, 'r', encoding='utf-8') as handle:
            data = yaml.safe_load(handle)
        self.get_logger().info(
            'Dead reckoning mode: odom frame, max speed %.2f m/s',
            self.max_speed)
        for wp in data['waypoints']:
            self.get_logger().info('Waypoint: %s', wp.get('name', 'unnamed'))
            self.move_to(
                float(wp['x']),
                float(wp['y']),
                float(wp.get('yaw', 0.0)))
        self.get_logger().info('All waypoints finished')


def main(args=None):
    rclpy.init(args=args)
    node = DeadReckoningFollower()
    try:
        if len(sys.argv) < 2:
            node.get_logger().error(
                'Usage: follow_waypoints_dead_reckoning.py waypoints.yaml')
            return
        node.run(sys.argv[1])
    finally:
        node.publisher.publish(Twist())
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
