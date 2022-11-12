#!usr/bin/env python3 

# refer my_first_node to understand the structure of the python file
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist         #the type in the ros topic info is geometry_msgs/msg/Twist

class DrawCircleNode(Node):

    def __init__(self):
        super().__init__("draw_circle")
        self.cmd_vel_pub = self.create_publisher()   #to create a publisher
        self.get_logger().info("draw circle")

def main(args=None):
    rclpy.init(args=args)
    node = DrawCircleNode()
    rclpy.shutdown()

if __name__ == '__main__':
    main()