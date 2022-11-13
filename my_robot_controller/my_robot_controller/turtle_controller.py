#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class TurtleControllerNode(Node):

    def __init__(self):
        super().__init__("turtle_controller")
        self._logger().info("Turtle controller has been started")



def main(args=None):
    rclpy.init(args=args)
    node = TurtleControllerNode()
    rclpy.spin()
    rclpy.shutdown()