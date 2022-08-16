#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import rospy
from std_msgs.msg import String
from fucking_biip import Buzzer

class Button:
	def __init__(self):
		rospy.init_node("button_node")
		rospy.loginfo("Starting Button NODE")

		GPIO.setmode(GPIO.BCM)
		GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.add_event_detect(18, GPIO.FALLING)
		GPIO.add_event_callback(18, self.button_callback)

		self.button_pub = rospy.Publisher("/Rasp_PI/Button_start", String, queue_size=10)

		self.inputValue = String()
		self.inputValue.data = 'End'
		self.lastInputValue = False
		self.inputCount = 0

		self.song = Buzzer(4)

	def spin(self):
		while not rospy.is_shutdown():
			rospy.loginfo(self.inputValue)
			self.button_pub.publish(self.inputValue)


	def button_callback(self, msg):
		if self.lastInputValue == 'Start':
			self.inputValue.data = 'End'
			self.song.play_death()
		else:
			self.inputValue.data = 'Start'
			self.song.play_start()
		self.lastInputValue = self.inputValue.data


if __name__ == "__main__":
	button_node = Button()
	button_node.spin()


