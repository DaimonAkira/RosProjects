#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32

def callback(message):
    V_left = message.data + 10
    V_right = message.data - 10
    rospy.loginfo("Left = %f  , Right = %f", V_left , V_right)

# ---------------------------------------------------
rospy.init_node("robot_controller_motor_controller", anonymous=True)
rospy.Subscriber("/cmd_vel", Float32, callback)
rospy.spin()