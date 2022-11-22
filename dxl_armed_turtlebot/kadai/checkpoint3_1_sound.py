#!/usr/bin/env python

import rospy
from kobuki_msgs.msg import Sound

if __name__ == '__main__':
    rospy.init_node("checkpoint1_3_2_sound_python", anonymous=True)

    pub = rospy.Publisher("/mobile_base/commands/sound", Sound, queue_size=1)
    rospy.sleep(1)

    msg = Sound()
    for i in range(6):
        msg.value = i+1
        rospy.loginfo("publish msg [value: %d]"%(msg.value))
        pub.publish(msg)
        rospy.sleep(1)
    msg.value = 0
    rospy.loginfo("publish msg [value: %d]"%(msg.value))
    pub.publish(msg)