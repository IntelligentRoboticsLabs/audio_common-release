#!/usr/bin/env python
"""
Simple example showing how to use the SoundClient provided by libsoundplay,
in blocking, non-blocking, and explicit usage.
"""
import rospy
from sound_play.libsoundplay import SoundClient
from sound_play.srv import Talk

class SoundClientRos:
    def __init__(self):
        s = rospy.Service('/gb_dialog/talk', Talk, self.talkCallback)
    def talkCallback(self,req):
        soundhandle = SoundClient(blocking=True)
        soundhandle.say(req.str)
        return []

if __name__ == '__main__':
    rospy.init_node('ros_soundclient', anonymous=False)
    sound_client = SoundClientRos()
    try:
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
