import rospy
from std_msgs.msg import String

def callback(msg):
    print(msg.data)

test_pub = rospy.Publisher("Test", String, queue_size=10)
rospy.Subscriber("Test", Type, callback)

test_class = String()
test.data = "Start"

test_pub.pub(test_class)