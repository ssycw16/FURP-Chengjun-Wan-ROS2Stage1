#!/usr/bin/env python3

import sys

import rclpy
import yaml

from send_goal import GoalSender


def main(args=None):
    rclpy.init(args=args)
    node = GoalSender()
    try:
        if len(sys.argv) < 2:
            node.get_logger().error(
                'Usage: send_multiple_goals.py waypoints.yaml')
            return
        with open(sys.argv[1], 'r', encoding='utf-8') as handle:
            data = yaml.safe_load(handle)
        for wp in data['waypoints']:
            node.get_logger().info('Waypoint: %s', wp.get('name', 'unnamed'))
            ok = node.send_goal(
                float(wp['x']),
                float(wp['y']),
                float(wp.get('yaw', 0.0)),
                wp.get('frame_id', 'map'))
            if not ok:
                node.get_logger().warn('Failed at waypoint: %s', wp)
                break
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
