#!usr/bin/env python3 

#interpreter line to tell the interpreter to use python3

import rclpy #similar to rospy
from rclpy.node import Node

class MyNode(Node): #this class inherits from Node from rclpy.node, so that it can access to all the functions from Node

    def __init__(self):  #create a constructor
        super().__init__("first_node")   # the command - super calles the constructor of the upper class, we enter the nodes name inside bracketm
        #the above statement initiallizes the node
        self.get_logger().info("hello from ROS2") # to print hello world

def main(args=None):  #arguments are set to none by default
    rclpy.init(args=args) #init the rclpy communication, args of init function are that we get from main
    node = MyNode()   # we create the node here
    rclpy.spin(node) # to run continusly untill killed
    rclpy.shutdown() # shut down the rclpy communication

if __name__ == '__main__':
    main()