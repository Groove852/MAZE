#!/usr/bin/python3
import rospy
from sensor_msgs.msg import LaserScan

class Mapping(object):
    def __init__(self):
        rospy.init_node("map_filter")

        self.laserScan = LaserScan()
        self.rate = 10
        self.ranges = [0] * 360

        rospy.Subscriber("scan", LaserScan, self.mapping)
        self.mapPub = rospy.Publisher("/Filters/Mapping", LaserScan, queue_size=10)

    def spin(self):
        r = rospy.Rate(self.rate)
        while not rospy.is_shutdown():
            self.mapPub.publish(self.laserScan)
            rospy.loginfo(len(self.laserScan.ranges))
            # self.laserScan = LaserScan()
            r.sleep()

    def mapping(self, msg):
        self.laserScan.angle_min = msg.angle_min
        self.laserScan.angle_max = msg.angle_max
        self.laserScan.angle_increment = msg.angle_increment
        self.laserScan.time_increment = msg.time_increment
        self.laserScan.scan_time = msg.scan_time
        self.laserScan.range_min = msg.range_min
        self.laserScan.range_max = msg.range_max
        self.laserScan.intensities = msg.intensities
        for i in range(0, 360):
            self.ranges[i] = (msg.ranges[i] - self.laserScan.range_min) * ((10 - 0) / (self.laserScan.range_max - self.laserScan.range_min))
        self.laserScan.ranges = self.ranges

if __name__ == "__main__":
    mapping = Mapping()
    mapping.spin()