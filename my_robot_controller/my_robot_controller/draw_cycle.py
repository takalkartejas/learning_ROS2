#!usr/bin/env python3 

# refer my_first_node to understand the structure of the python file
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist         #the type in the ros topic info is geometry_msgs/msg/Twist

class DrawCircleNode(Node):

    def __init__(self):
        super().__init__("draw_circle")
        self.cmd_vel_pub = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)   #to create a publisher, 10 is a queue size to create a buffer in case of bad network
        self.get_logger().info("draw circle")
        self.timer_ = self.create_timer(0.5, self.send_velocity_callback)

    def send_velocity_callback(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        self.cmd_vel_pub.publish(msg)    #publish is the method from the publisher we created

def main(args=None):
    rclpy.init(args=args)
    node = DrawCircleNode()
    rclpy.spin(node)
    rclpy.shutdown()
    

if __name__ == '__main__':
    main()