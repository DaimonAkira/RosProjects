#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

rospy.init_node("turtlesim", anonymous=True)
pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

rate = rospy.Rate(100)
command = Twist()

while not rospy.is_shutdown(): 
    command.linear.x = 0.5
    command.linear.y = 0
    command.linear.z = 0
    command.angular.x = 0
    command.angular.y = 0
    command.angular.z = 1
    pub.publish(command)
    rate.sleep()