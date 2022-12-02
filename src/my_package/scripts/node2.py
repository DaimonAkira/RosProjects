#!/usr/bin/env python3
import rospy

def node2():
    rospy.init_node('node2', anonymous=True)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        print("Node 2 is running.")
        rate.sleep()

if __name__ == '__main__':
    try:
        node2()
    except rospy.ROSInterruptException:
        pass