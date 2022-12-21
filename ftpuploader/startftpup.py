# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 11:34:01 2022

@author: Akira
"""
#!/usr/bin/env python3
import rospy
import os
import runpy


def run(runfile):
  with open(runfile,"r") as rnf:
    exec(rnf.read())


def node2():
    rospy.init_node('node2', anonymous=True)
    rate = rospy.Rate(1/30)

    while not rospy.is_shutdown():
        print("FTP Uploader running.")
        os.system("exec /home/tesla/catkin_ws/src/ftpuploader/scripts/ftpup.py")
        rate.sleep()

if __name__ == '__main__':
    try:
        node2()
    except rospy.ROSInterruptException:
        pass

