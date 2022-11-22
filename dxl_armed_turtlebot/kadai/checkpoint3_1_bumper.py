#!/usr/bin/env python

import rospy
from kobuki_msgs.msg import ButtonEvent

def bumper_cb(msg):
    button = msg.bumper
    state = msg.state
    rospy.loginfo("subscribe msg [button: %d  state: %d]"%(button, state))
    
if __name__ == '__main__':
    rospy.init_node("checkpoint3_1_bumper_python", anonymous=True)

    rospy.Subscriber("/mobile_base/events/bumper", BumperEvent, bumper_cb)

    rospy.spin()
