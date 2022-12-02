#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32

rospy.init_node("robot_controller_vel_publisher", anonymous=True)
pub = rospy.Publisher("/cmd_vel", Float32, queue_size=10)

rate = rospy.Rate(10)

while not rospy.is_shutdown(): 
    pub.publish(11.5)
    rate.sleep()