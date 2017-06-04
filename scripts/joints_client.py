#!/usr/bin/env python

from baxter_arm.srv import *
from sensor_msgs.msg import JointState
import rospy

'''
client that requests the current position of a joint from the
joint states server
'''

def joint_client(x):
	print "joint_client called by passing: "
	print x
	rospy.wait_for_service('joint_state_finder')
	try:
		joint_state_serv = rospy.ServiceProxy('joint_state_finder', Joint_position)

		response = joint_state_serv(x)
		return response.joint_state
	except rospy.ServiceException, e:
		print "Service call failed: %s"%e



def usage():
	return "%s [x]"%sys.argv[0]




if __name__=='__main__':
	if len(sys.argv) == 2:
		joint = str(sys.argv[1])
		#print "parameter passed is "
		#print joint
	else:
		print usage()
		sys.exit(1)
	print "Requesting"
    	print (joint_client(joint))
