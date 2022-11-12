#!usr/bin/env python3 

# refer my_first_node to understand the structure of the python file
import rclpy
from rclpy.node import Node

class PoseSubscriberNode(Node):

    def __init__(self):
        super().__init__("pose_subscriber")
        self.get_logger().info("draw circle")
        self.timer_ = self.create_timer(0.5, self.send_velocity_callback)

    def send_velocity_callback(self):

def main(args=None):
    rclpy.init(args=args)
    node = PoseSubscriberNode()
    rclpy.spin(node)
    rclpy.shutdown()
    

if __name__ == '__main__':
    main()