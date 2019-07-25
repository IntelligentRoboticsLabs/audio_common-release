#!/usr/bin/env python
"""
Simple example showing how to use the SoundClient provided by libsoundplay,
in blocking, non-blocking, and explicit usage.
"""
import rospy
from sound_play.libsoundplay import SoundClient
from sound_play.srv import Talk
from std_srvs.srv import Empty

class SoundClientRos:
    def __init__(self):
        s = rospy.Service('/gb_dialog/talk', Talk, self.talkCallback)
        s = rospy.Service('/gb_dialog/listen_sound', Empty, self.listenSoundCallback)
        self.soundhandle = SoundClient(blocking=True)

    def talkCallback(self,req):
        self.soundhandle.say(req.str)
        return []
    def listenSoundCallback(self,req):
        self.soundhandle.play(3, 1.0)
        return []
if __name__ == '__main__':
    rospy.init_node('ros_soundclient', anonymous=False)
    sound_client = SoundClientRos()
    try:
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
