#!usr/bin/env python3 

# refer my_first_node to understand the structure of the python file
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose  # Type: turtlesim/msg/Pose

class PoseSubscriberNode(Node):

    def __init__(self):
        super().__init__("pose_subscriber")
        self.pose_subscriber = self.create_subscription(Pose, "/turtle1/pose", self.pose_callback, 10 ) # 10 is a buffer, Pose is a messegem /turtle1/pose is a topic
    
    def pose_callback(self, msg: Pose):    #msg is of type Pose
        self.get_logger().info(str(msg))

def main(args=None):
    rclpy.init(args=args)
    node = PoseSubscriberNode()
    rclpy.spin(node)
    rclpy.shutdown()
    

if __name__ == '__main__':
    main()