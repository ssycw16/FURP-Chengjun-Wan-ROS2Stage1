from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import Command
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    pkg_name = "carter_description"
    pkg_share_path = get_package_share_directory(pkg_name)
    xacro_file_path = os.path.join(pkg_share_path, "urdf", "carter.urdf.xacro")

    robot_description_param = ParameterValue(
        Command(["xacro ", xacro_file_path]),
        value_type=str
    )

    robot_state_pub = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{"robot_description": robot_description_param}]
    )

    joint_gui = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui"
    )

    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        output="screen"
    )

    return LaunchDescription([robot_state_pub, joint_gui, rviz_node])
