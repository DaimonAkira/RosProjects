#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

rospy.init_node("publisher_node", anonymous=True)
pub = rospy.Publisher("name_of_the_topic", Int32, queue_size=10)

rate = rospy.Rate(10)
count = Int32()
count.data = 0

while not rospy.is_shutdown(): 
    pub.publish(count)
    count.data = count.data + 1
    rate.sleep()