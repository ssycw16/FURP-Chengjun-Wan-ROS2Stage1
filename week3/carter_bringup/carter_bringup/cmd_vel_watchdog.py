#!/usr/bin/env python3

import rclpy
from geometry_msgs.msg import Twist
from rclpy.node import Node


class CmdVelWatchdog(Node):
    """Publish zero velocity when no new cmd_vel is received in time."""

    def __init__(self):
        super().__init__('cmd_vel_watchdog')
        self.declare_parameter('timeout', 0.5)
        self.declare_parameter('check_rate', 20.0)

        self.timeout = self.get_parameter('timeout').value
        check_rate = self.get_parameter('check_rate').value
        self.last_command_time = self.get_clock().now()
        self.stopped = False

        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        self.subscription = self.create_subscription(
            Twist, 'cmd_vel', self.on_cmd_vel, 10)
        self.timer = self.create_timer(1.0 / check_rate, self.check)

    def on_cmd_vel(self, msg):
        if abs(msg.linear.x) > 1e-6 or abs(msg.linear.y) > 1e-6 or \
                abs(msg.angular.z) > 1e-6:
            self.last_command_time = self.get_clock().now()
            self.stopped = False

    def check(self):
        elapsed = (self.get_clock().now() - self.last_command_time).nanoseconds
        if elapsed * 1e-9 > self.timeout and not self.stopped:
            self.get_logger().warn('No cmd_vel received, sending zero velocity')
            self.publisher.publish(Twist())
            self.stopped = True


def main(args=None):
    rclpy.init(args=args)
    node = CmdVelWatchdog()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
