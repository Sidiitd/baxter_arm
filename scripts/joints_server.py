#!/usr/bin/env python
import rospy
from baxter_arm.srv import *
from sensor_msgs.msg import JointState

#names = {}
joint_states = {}
#class JointStateFinder(object):
def joint_state_server():
		rospy.init_node('joint_state_server')
		#self.current_joint_states = None
		#self.joint_requested = req
		sub  = rospy.Subscriber('/robot/joint_states', JointState, joint_state_cb, queue_size=1)
		serv = rospy.Service('joint_state_finder', Joint_position, service_handler)
		
		#names = {'head_pan', 'l_gripper_l_finger_joint', 'l_gripper_r_finger_joint', 'left_e0', 'left_e1', 'left_s0', 'left_s1', 'left_w0', 'left_w1', 'left_w2', 'r_gripper_l_finger_joint', 'r_gripper_r_finger_joint', 'right_e0', 'right_e1', 'right_s0', 'right_s1'}
		rospy.loginfo('ready for returning the state of the required joint')
		rospy.spin()


def joint_state_cb(data):
		global joint_states
		#joint_states = data.position
		j=0
		while j<len(data.name):
			joint_states[data.name[j]] = data.position[j]
			j +=1

		#rospy.loginfo("printing from joint_state callback")
		#rospy.loginfo(len(joint_states))


def service_handler(request):
		#self.joint_requested = request
		global joint_states
		rospy.loginfo("Request handler called")
		#dict = {}
		#i = 0
		try:
			print "trying"
			#print size(names)
			'''
			while i<len(names):
				print "Printing from inside of while loop"
				print names[1]
				print joint_states[0]
				#rospy.loginfo("the length of names is %i"len(name))
				dict[names[i]] = joint_states[i]
				print "first assignment successful"
				i +=1
			#print joint_states[1]
			'''
			#print len(joint_states)
			print request.joint_to_check
			print "The server says: the position of joint you requested is" + str(joint_states[request.joint_to_check])
			return joint_states[request.joint_to_check]
		except Exception:
			print " Service call failed"



		
			

'''
	def run(self):
		
	   rate = rospy.Rate(0.2)
	   while not rospy.is_shutdown():
            	self.do_work()
            	rate.sleep()
 		

'''

if __name__=="__main__":
	'''
	rospy.init_node('joint_state_server')
	j = JointStateFinder()
	j.run()
	'''
	joint_state_server()

