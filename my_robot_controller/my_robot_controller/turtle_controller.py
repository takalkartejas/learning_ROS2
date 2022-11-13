#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class TurtleControllerNode(Node):

    def __init__(self):
        super().__init__("turtle_controller")
        self.get_logger().info("Turtle controller has been started")
        self.pose_subscriber = self.create_subscription(Pose,'/turtle1/Pose',self.pose_callback, 10)
        self.vel_publisher = self.create_publisher(Twist,'/turtle1/cmd_vel', 10)
        self.create_timer(1,self.vel_publisher_callback)

    def pose_callback(self, pose: Pose):
        self.get_logger().info(str(pose))

    def vel_publisher_callback(self, msg: Twist):
        msg.linear.x = 0.1
        msg.angular.z = 0.1
        self.vel_publisher.publish(msg)



def main(args=None):
    rclpy.init(args=args)
    node = TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()