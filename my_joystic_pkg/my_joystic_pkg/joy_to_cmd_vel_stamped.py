#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from geometry_msgs.msg import TwistStamped

class JoyToCmdVelStamped(Node):
    def __init__(self):
        super().__init__('joy_to_cmd_vel_stamped')
        self.declare_parameter("linear_factor", 1.0)
        self.declare_parameter("angular_factor", 1.0)
        self.linear_factor = self.get_parameter("linear_factor").value
        self.angular_factor = self.get_parameter("angular_factor").value

        self.subscription = self.create_subscription(
            Joy, 'joy', self.joy_callback, 10)
        self.publisher = self.create_publisher(TwistStamped, 'cmd_vel', 10)

        self.get_logger().info("Joystick to TwistStamped node has been started.")

    def joy_callback(self, msg):
        # Joystick to cmd_vel_stamped mapping logic
        linear_x = msg.axes[3]  # Adjust based on joystick configuration
        angular_z = msg.axes[2]  # Adjust based on joystick configuration

        cmd_vel_msg = TwistStamped()
        cmd_vel_msg.header.stamp = self.get_clock().now().to_msg()
        cmd_vel_msg.header.frame_id = "base_link"
        cmd_vel_msg.twist.linear.x = linear_x * self.linear_factor
        cmd_vel_msg.twist.angular.z = angular_z * self.angular_factor

        self.publisher.publish(cmd_vel_msg)


def main(args=None):
    rclpy.init(args=args)
    node = JoyToCmdVelStamped()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

