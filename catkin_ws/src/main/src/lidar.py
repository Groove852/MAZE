#!/usr/bin/python3
import os
import glob
import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import String


class Lidar:
    def __init__(self):
        rospy.init_node("lidar_serial_node")
        self._detecting_button = False
        self.count = True
        self.trying = True
        self.starting_count = 0
        self.rate = rospy.Rate(10)
        self.state = String()
        self.state.data = "Doesn't have start pushing"
        self.pub_state = rospy.Publisher("/Rasp_PI/LIDAR_State", String, queue_size=10)
        self.sub_button = rospy.Subscriber("/Rasp_PI/Button_start", String, callback=self.detect_button)

    def spin(self):
        while not rospy.is_shutdown():
            if self._detecting_button:
                if self.starting_count == 0:
                    if self.count:
                        if self.start():
                            rospy.loginfo(f'[+] Starting LIDAR are successfully')
                        self.count = False
                        self.state.data = "OK"
            else:
                if self.starting_count != 0:
                    rospy.loginfo(f'[-] Killing...')
                    os.popen('rosnode kill hlds_laser_publisher')
                    rospy.loginfo(f'[-] Killing LIDAR are successfully')
                    self.starting_count = 0
                    self.count = True
                    self.state.data = "NOT OK"
            self.pub_state.publish(self.state)
            self.rate.sleep()

    def start(self):
        if glob.glob('/dev/ttyUSB*'):
            os.system(f"sudo chmod a+rw {glob.glob('/dev/ttyUSB*')[0]}")
            self.starting_count += 1
            os.popen(f'roslaunch hls_lfcd_lds_driver hlds_laser.launch')
            return True

    def detect_button(self, msg):
        if msg.data == 'Start':
            self._detecting_button = True
        else:
            self._detecting_button = False


if __name__ == "__main__":
    lidar = Lidar()
    lidar.spin()