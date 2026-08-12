#!/usr/bin/env python3

import math

import rclpy
from geometry_msgs.msg import Twist
from rclpy.duration import Duration
from rclpy.node import Node


class RotateInPlace(Node):
    def __init__(self):
        super().__init__('rotate_in_place')
        self.declare_parameter('angular_speed', 0.5)
        self.declare_parameter('angle', 2.0 * math.pi)
        self.declare_parameter('direction', 'left')

        self.angular_speed = self.get_parameter('angular_speed').value
        self.angle = abs(self.get_parameter('angle').value)
        direction = self.get_parameter('direction').value
        self.sign = 1.0 if direction == 'left' else -1.0
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
        self.get_logger().info('Start in-place rotation')
        duration = self.angle / max(self.angular_speed, 1e-6)
        self.drive(0.0, self.sign * self.angular_speed, duration)
        self.get_logger().info('Rotation finished')


def main(args=None):
    rclpy.init(args=args)
    node = RotateInPlace()
    try:
        node.run()
    finally:
        node.publisher.publish(Twist())
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
