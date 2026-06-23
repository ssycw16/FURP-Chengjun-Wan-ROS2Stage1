from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    pub_node = Node(
        package="week1_pubsub",
        executable="publisher",
        name="simple_publisher",
        output="screen"
    )
    sub_node = Node(
        package="week1_pubsub",
        executable="subscriber",
        name="simple_subscriber",
        output="screen"
    )
    return LaunchDescription([pub_node, sub_node])
