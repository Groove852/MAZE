#!/usr/bin/python3
import smbus
import rospy
import sys
from std_msgs.msg import Int32
import time


class Sensor:
	def __init__(self):
		
		self.bus = smbus.SMBus((1))	
		# напиши два кода под каждый датчик, так будет проще чем с этим ебаться
		self.bit = sys.argv[1]
		
		if self.bit == '90':
			self.bit = 0x5a
			self.sensor_pub = rospy.Publisher(f'/Rasp_PI/Left_sensor', Int32, queue_size=10)
			rospy.init_node("Left_sensor_node")
			rospy.loginfo("Starting Left Sensor NODE")
		elif self.bit == '91':
			self.bit = 0x5b
			self.sensor_pub = rospy.Publisher(f'/Rasp_PI/Right_sensor', Int32, queue_size=10)
			rospy.init_node("Right_sensor_node")
			rospy.loginfo("Starting Right Sensor NODE")

		rospy.logdebug(sys.argv)
		self.sensor_value = Int32()
	
	def spin(self):
		if self.bit == None:
			rospy.logerr("Doesn't have bit value")
			rospy.logerr(f"{sys.argv}")
		else:
			while not rospy.is_shutdown():
				try:
					self.sensor_value.data = int((self.bus.read_byte_data(self.bit, 0x07) * 5 / 9) - 32)
				except OSError:
					pass
				self.sensor_pub.publish(self.sensor_value)
				rospy.loginfo(self.sensor_value)

if __name__ == "__main__":
	sensor_node = Sensor()
	sensor_node.spin()

