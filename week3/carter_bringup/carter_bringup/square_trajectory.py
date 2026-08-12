#!/usr/bin/env python3

import math

import rclpy
from geometry_msgs.msg import Twist
from rclpy.duration import Duration
from rclpy.node import Node


class SquareTrajectory(Node):
    def __init__(self):
        super().__init__('square_trajectory')
        self.declare_parameter('linear_speed', 0.2)
        self.declare_parameter('angular_speed', 0.5)
        self.declare_parameter('side_length', 0.6)

        self.linear_speed = self.get_parameter('linear_speed').value
        self.angular_speed = self.get_parameter('angular_speed').value
        self.side_length = self.get_parameter('side_length').value
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)

    def drive(self, linear, angular, duration):
        rate = self.create_rate(20)
        msg = Twist()
        msg.linear.x = linear
        msg.angular.z = angular
        end_time = self.get_clock().now() + Duration(seconds=duration)
        while self.get_clock().now() < end_time and rclpy.ok():
            self.publisher.publish(msg)
            rate.sleep()
        self.publisher.publish(Twist())

    def run(self):
        self.get_logger().info(
            'Square trajectory: side=%.2f m, v=%.2f m/s, w=%.2f rad/s',
            self.side_length, self.linear_speed, self.angular_speed)
        straight_time = self.side_length / max(self.linear_speed, 1e-6)
        turn_time = (math.pi / 2.0) / max(self.angular_speed, 1e-6)
        for _ in range(4):
            self.drive(self.linear_speed, 0.0, straight_time)
            self.drive(0.0, self.angular_speed, turn_time)
        self.drive(0.0, 0.0, 0.3)
        self.get_logger().info('Square trajectory finished')


def main(args=None):
    rclpy.init(args=args)
    node = SquareTrajectory()
    try:
        node.run()
    finally:
        node.publisher.publish(Twist())
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
