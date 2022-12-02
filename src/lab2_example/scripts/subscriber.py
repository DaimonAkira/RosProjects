#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def callback(message):
    rospy.loginfo("Count is = %i", message.data)

# ---------------------------------------------------
rospy.init_node("subscriber_node", anonymous=True)
rospy.Subscriber("name_of_the_topic", Int32, callback)
rospy.spin()