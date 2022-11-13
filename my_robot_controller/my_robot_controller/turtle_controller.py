#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.srv import SetPen
from functools import partial

class TurtleControllerNode(Node):

    def __init__(self):
        super().__init__("turtle_controller")
        self.previous_x_ = 0
        self.get_logger().info("Turtle controller has been started")
        self.pose_subscriber = self.create_subscription(Pose,'/turtle1/pose',self.pose_callback, 10)
        self.vel_publisher = self.create_publisher(Twist,'/turtle1/cmd_vel', 10)
        self.create_timer(1,self.vel_publisher_callback)

    def pose_callback(self, pose: Pose):
        self.x = pose._x
        self.y = pose._y
        #self.get_logger().info('x=' + str(self.x) + 'y=' + str(self.y))
        if self.x > 5.5 and self.previous_x_ <= 5.5:
            self.previous_x_ = pose.x
            self.get_logger().log("set colour to red")
            self.call_set_pen_service(255,0,0,3,0)
        if self.x <=5.5 and self.previous_x_ > 5.5:
            self.previous_x_ = pose.x
            self.get_logger().log("set colour to green")
            self.call_set_pen_service(0,255,0,3,0)
            

    def vel_publisher_callback(self):
        msg = Twist()

        if self.x >9.0 or self.x < 1.0 or self.y > 9.0 or self.y < 1.0:
            msg.linear.x = 0.5
            msg.angular.z = 0.5
        else:
            msg.linear.x = 0.5
            msg.angular.z = 0.0
        self.vel_publisher.publish(msg)


    def call_set_pen_service(self,r,g,b,width,off):
        client = self.create_client(SetPen, "/turtle1/set_pen")
        while not client.wait_for_service(1.0):   #if no client for 1 sec
            self.get_logger().warn("waiting for service...")  #then print this

        request = SetPen.Request()
        request.r = r
        request.g = g
        request.b = b
        request.width = width
        request.off = off

        future  = client.call_async(request)   # we can call service asyncronasly, the node will not be blocked using a callback
        future.add_done_callback(partial(self.callback_set_pen)) 

    def callback_set_pen(self, future): #to call back when response is recieved from service
        try:
            response = future.result()
        except Exception as err:
            self.get_logger().error("service call failed %r" % (err,))

def main(args=None):
    rclpy.init(args=args)
    node = TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()