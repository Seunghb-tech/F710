#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

class JoyToCmdVel(Node):
    def __init__(self):
        super().__init__('joy_to_cmd_vel')
        self.declare_parameter("linear_factor", 1)
        self.declare_parameter("angular_factor", 1)
        self.linear_factor = self.get_parameter("linear_factor").value
        self.angular_factor = self.get_parameter("angular_factor").value
        self.subscription = self.create_subscription(
            Joy, 'joy', self.joy_callback, 10)
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        self.get_logger().info("joystic_subscriber has been started.")

    def joy_callback(self, msg):
        # Define your joystick to cmd_vel mapping logic here
        linear_x = msg.axes[3]  # Adjust this according to your joystick
        angular_z = msg.axes[2]  # Adjust this according to your joystick

        cmd_vel_msg = Twist()
        cmd_vel_msg.linear.x = linear_x * self.linear_factor
        cmd_vel_msg.angular.z = angular_z * self.angular_factor

        self.publisher.publish(cmd_vel_msg)


def main(args=None):
    rclpy.init(args=args)
    node = JoyToCmdVel()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
