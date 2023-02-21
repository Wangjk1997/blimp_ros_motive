import rospy
from geometry_msgs.msg import PoseStamped
from functools import partial

class BlimpState:
    def __init__(self, num=1):
        self.num = num
        self.stateList = dict()

    def pullData(self, data, id):
        self.stateList[id] = data
        #print(self.stateList)
        print(type(data.pose.position))
    
    def addSubscriber(self, name="/vrpn_client_node"):
        rospy.init_node('listener', anonymous=True)
        for index in range(self.num):
            tmpName = name + "/Blimp" + str(index + 1) + "/pose"
            rospy.Subscriber(tmpName, PoseStamped, partial(self.pullData, id=("Blimp" + str(index + 1))))

def main():
    myBlimp = BlimpState(2)
    myBlimp.addSubscriber()
    rospy.spin()

if __name__=='__main__':
    main()    
        