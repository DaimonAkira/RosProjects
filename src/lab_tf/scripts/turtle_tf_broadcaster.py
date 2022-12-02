#!/usr/bin/env python  
import rospy
import tf
import turtlesim.msg as turtlebotmsgs


def callback_function(msg):
    br = tf.TransformBroadcaster()
    br.sendTransform((msg.x, msg.y, 0),
                     tf.transformations.quaternion_from_euler(0, 0, msg.theta),
                     rospy.Time.now(),
                     "turtle",
                     "world")
   

rospy.init_node('turtle_tf_broadcaster')
rospy.Subscriber("/turtle1/pose", turtlebotmsgs.Pose, callback_function)
rospy.spin()


