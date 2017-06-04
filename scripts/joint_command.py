#!/usr/bin/env python
import rospy
from baxter_core_msgs.msg import JointCommand


def main():
	rospy.init_node('baxter_arm')
	rospy.loginfo('main method called')
	rate = rospy.Rate(10)
	pub = rospy.Publisher('/robot/limb/left/joint_command', JointCommand, queue_size=1)
	
	while not rospy.is_shutdown():
		msg = JointCommand()
		msg.mode = msg.POSITION_MODE
		msg.names = {'right_s0', 'right_s1', 'right_w0', 'right_w1', 'right_w2', 'right_e0', 'right_e1'}
		msg.command = {0.0,0.0,0.1,0.1,0.0,0.0,0.0}
		pub.publish(msg)
		rate.sleep()


if __name__ == '__main__':
		rospy.loginfo('Initialising node....')
		try:
			main()
		except rospy.ROSInterruptException:
			pass