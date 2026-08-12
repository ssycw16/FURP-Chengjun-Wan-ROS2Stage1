#!/usr/bin/env python3

import csv
import math

import rclpy
from nav_msgs.msg import Odometry
from rclpy.node import Node


class CompareOdometry(Node):
    def __init__(self):
        super().__init__('compare_odometry')
        self.declare_parameter('output_file', 'odom_comparison.csv')
        self.output_file = self.get_parameter('output_file').value
        self.latest_raw = None
        self.rows = []
        self.max_diff = 0.0

        self.create_subscription(Odometry, 'odom', self.on_raw, 10)
        self.create_subscription(
            Odometry, 'odometry/filtered', self.on_filtered, 10)

    def yaw(self, msg):
        q = msg.pose.pose.orientation
        return 2.0 * math.atan2(q.z, q.w)

    def on_raw(self, msg):
        self.latest_raw = msg

    def on_filtered(self, msg):
        if self.latest_raw is None:
            return
        raw = self.latest_raw
        filtered = msg
        rx = raw.pose.pose.position.x
        ry = raw.pose.pose.position.y
        fx = filtered.pose.pose.position.x
        fy = filtered.pose.pose.position.y
        diff = math.hypot(rx - fx, ry - fy)
        self.max_diff = max(self.max_diff, diff)
        stamp = filtered.header.stamp
        row = [
            f'{stamp.sec}.{stamp.nanosec:09d}',
            f'{rx:.6f}', f'{ry:.6f}', f'{self.yaw(raw):.6f}',
            f'{fx:.6f}', f'{fy:.6f}', f'{self.yaw(filtered):.6f}',
            f'{diff:.6f}',
        ]
        self.rows.append(row)
        self.get_logger().info(
            'raw=(%.3f, %.3f) filtered=(%.3f, %.3f) diff=%.3f',
            rx, ry, fx, fy, diff)

    def save(self):
        with open(self.output_file, 'w', newline='') as handle:
            writer = csv.writer(handle)
            writer.writerow([
                'stamp', 'raw_x', 'raw_y', 'raw_yaw',
                'filtered_x', 'filtered_y', 'filtered_yaw', 'position_diff',
            ])
            writer.writerows(self.rows)
        self.get_logger().info(
            'Saved %d rows to %s, max position diff=%.3f m',
            len(self.rows), self.output_file, self.max_diff)


def main(args=None):
    rclpy.init(args=args)
    node = CompareOdometry()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.save()
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
