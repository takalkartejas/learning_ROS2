#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class TurtleControllerNode(Node):

    def __init__(self):
        super().__init__("turtle_controller")
        self.get_logger().info("Turtle controller has been started")
        self.pose_subscriber = self.create_subscription(Pose,'/turtle1/pose',self.pose_callback, 10)
        self.vel_publisher = self.create_publisher(Twist,'/turtle1/cmd_vel', 10)
        self.create_timer(1,self.vel_publisher_callback)

    def pose_callback(self, pose: Pose):
        self.x = pose._x
        self.y = pose._y
        #self.get_logger().info('x=' + str(self.x) + 'y=' + str(self.y))

    def vel_publisher_callback(self):
        msg = Twist()

        if self.x >9.0 or self.x < 1.0 or self.y > 9.0 or self.y < 1.0:
            msg.linear.x = 0.5
            msg.angular.z = 0.5
        else:
            msg.linear.x = 0.5
            msg.angular.z = 0.0
        self.vel_publisher.publish(msg)



def main(args=None):
    rclpy.init(args=args)
    node = TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()