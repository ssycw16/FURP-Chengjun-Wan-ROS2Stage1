#!/usr/bin/env python3

import math

import rclpy
from nav_msgs.msg import Odometry
from rclpy.node import Node
from tf2_ros import Buffer, TransformListener
from tf2_ros import ConnectivityException, ExtrapolationException, LookupException


class CheckOdomTf(Node):
    def __init__(self):
        super().__init__('check_odom_tf')
        self.latest_odom = None
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)
        self.odom_sub = self.create_subscription(
            Odometry, 'odom', self.on_odom, 10)
        self.timer = self.create_timer(1.0, self.check)

    def on_odom(self, msg):
        self.latest_odom = msg

    def check(self):
        if self.latest_odom is None:
            self.get_logger().warn('No /odom message received yet')
            return
        pose = self.latest_odom.pose.pose
        self.get_logger().info(
            'odom: x=%.3f y=%.3f yaw=%.3f',
            pose.position.x,
            pose.position.y,
            2.0 * math.atan2(pose.orientation.z, pose.orientation.w))
        try:
            transform = self.tf_buffer.lookup_transform(
                'odom', 'base_link', rclpy.time.Time())
            self.get_logger().info(
                'tf odom->base_link: t=(%.3f, %.3f, %.3f)',
                transform.transform.translation.x,
                transform.transform.translation.y,
                transform.transform.translation.z)
        except (LookupException, ConnectivityException,
                ExtrapolationException) as exc:
            self.get_logger().warn('TF lookup failed: %s', str(exc))


def main(args=None):
    rclpy.init(args=args)
    node = CheckOdomTf()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
