import rospy
from geometry_msgs.msg import PoseStamped
from functools import partial


def callback(data, id):
    print(data.pose.position)
    print(id)


def main():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/vrpn_client_node/Blimp1/pose", PoseStamped, partial(callback, id=1))
    rospy.spin()
    
if __name__=='__main__':
    main()
