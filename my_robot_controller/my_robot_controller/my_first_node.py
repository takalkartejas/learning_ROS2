#!usr/bin/env python3 
#interpreter line to tell the interpreter to use python3

import rclpy #similar to rospy

def main(args=None):  #arguments are set to none by default
    rclpy.init(args=args) #init the rclpy communication, args of init function are that we get from main


    rclpy.shutdown() # shut down the rclpy communication

if __name__ == '__main__':
    main()