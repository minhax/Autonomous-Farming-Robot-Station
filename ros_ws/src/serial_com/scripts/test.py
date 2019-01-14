#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from custom_msgs.msg import PlantBox

def talker():
	pub = rospy.Publisher('/image/plantbox_send', PlantBox, queue_size=10)
	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(1) # 10hz
	while not rospy.is_shutdown():
		msg = PlantBox()
		msg.x = 1
		msg.y = 2
		msg.length = 3
		msg.width = 4        
		pub.publish(msg)
		rate.sleep()

if __name__ == '__main__':
	talker()
