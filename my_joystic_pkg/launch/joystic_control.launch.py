import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'joystick_dev',
            default_value="/dev/input/js0",  # Adjust to your joystick device
            description="Path to the joystick device"),
        DeclareLaunchArgument(
            'joystick_deadzone',
            default_value="0.12",
            description="Joystick deadzone value"),
        
        Node(
            package='joy',
            executable='joy_node',
            name='joy_node',
            namespace='',
            output='screen',
            parameters=[{
                'dev': LaunchConfiguration('joystick_dev'),
                'deadzone': LaunchConfiguration('joystick_deadzone'),
            }]
        ),

        Node(
            package='my_joystic_pkg',  # Replace 'your_package' with your actual package name
            executable='joy_to_cmd_vel_node',
            name='joy_to_cmd_vel_node',
            namespace='',
            output='screen',
            remappings=[('/joy', 'joy'), ('/cmd_vel', 'cmd_vel')],
        )
    ])
