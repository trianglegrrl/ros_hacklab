#!/usr/bin/env python
	
"""
(C) 2011 Alaina Hardie, 9th Sense Robotics/Hacklab Toronto

WHAT IT DOES
------------------------------------------------------------------
Sends published commands (from /train_overlord/cmd) 
to Train Overlord and publishes anything he says to
/train_overlord/response 

WHAT IT REQUIRES
------------------------------------------------------------------
pySerial, http://pyserial.sourceforge.net/

WHAT YOU CAN DO WITH IT
------------------------------------------------------------------
This work is licensed under the Creative Commons 
Attribution-NonCommercial-ShareAlike 3.0 Unported License. 
To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/3.0/ 
or send a letter to Creative Commons, 444 Castro Street, 
Suite 900, Mountain View, California, 94041, USA.
"""

import roslib; roslib.load_manifest('train_overlord_controller')
import rospy
import serial

from std_msgs.msg import String

rospy.init_node('train_overlord_listener', anonymous=True)
toFeedback = rospy.Publisher ('/train_overlord/response', String)

s = serial.Serial('/dev/ttyUSB1', 9600)
s.g
def sendCommandToTrainOverlord(theData):
		s.write(theData)
		line = s.readline()
		toFeedback.publish(String(line))

def receivedCommandCallback(data):
	sendCommandToTrainOverlord(data.data)

def listener():
	rospy.Subscriber("/train_overlord/cmd", String, receivedCommandCallback)
	rospy.spin()

if __name__ == '__main__':

	listener()



