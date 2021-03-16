#! /usr/bin/python3

import rospy
import tf_conversions
import tf2_ros
from turtlesim.msg import Pose
import geometry_msgs.msg

def handle_turtle_pose(msg, turtlename):
    br = tf2_ros.TransformBroadcaster()
    transform = geometry_msgs.msg.TransformStamped()
    

if __name__ == '__main__ :
    rospy.init_node('tf2 turtle_broadcaster')
    turtlename = rospy.get_param('~turtle')
    rospy.Subscriber('/%s/pose' % turtlename,
                    Pose,
                    handle_turtle_pose,
                    turtlename)
    rospy.spin()   