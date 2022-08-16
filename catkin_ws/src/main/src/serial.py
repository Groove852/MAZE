#!/usr/bin/python3

import os
import rospy
from sensor_msgs.msg import LaserScan

class Serial:
    def __init__(self):
        rospy.init_node("lidar_serial_node")
        self._port = "/dev/ttyACM"
        self._baud = 115200
        self._detecting = True
        self.__count = 0
        self._number = 0

    def spin(self):
        rospy.loginfo(f'[+] Starting of serial are successfully')
        self.start()
        # while not rospy.is_shutdown():
        #     if self.__count == 0:

    def start(self):
        # os.system(f"sudo chmod a+rw {self._port}{self._number}")
        os.system(f'rosrun rosserial_python serial_node.py _port:=/dev/ttyACM{self._number} _baud:={self._baud}')

if __name__ == "__main__":
    serial = Serial()
    serial.spin()
