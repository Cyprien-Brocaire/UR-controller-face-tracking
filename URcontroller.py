import struct
import socket
from math import pi, degrees, sqrt
import URBasic
import time
def normeU(x):
    if x != 0:
        return x/sqrt(x**2)
    else :
        return 0

def norme(x):
    if x != 0:
        return sqrt(x**2)
    else :
        return 0
speed = 3000
acc = 0.3
vel = 0.3
class URobot(URBasic.urScriptExt.UrScriptExt):
    def run(self):
        self.reset_error()
        print(self.get_actual_joint_positions())
        self.movej(q=[0, -pi, pi/2, -pi/2, pi/2, 0], a=2, v=20, wait=True)

    def tracking_translation(self, delta):
        print(delta)
        self.reset_error()
        pose = self.get_actual_tcp_pose()
        pose[1] -= delta[0]/10000
        pose[2] -= delta[1]/10000

        self.set_realtime_pose(pose=pose)
        #self.movel(pose=pose, a=acc, v=vel, wait=True)

    def tracking_rotation(self, delta):
        print("CCC")
        print(delta)
        self.reset_error()
        pose = self.get_actual_tcp_pose()
        pose[3] += normeU(delta[0])*(156/220) * norme(delta[0]/speed)
        pose[4] += normeU(delta[0])           * norme(delta[0]/speed)  
        pose[5] -= normeU(delta[0])           * norme(delta[0]/speed)

        pose[3] -= normeU(delta[1])           * norme(delta[1]/speed)  
        pose[4] += normeU(delta[1])           * norme(delta[1]/speed)
        pose[5] += normeU(delta[1]) *(156/220)* norme(delta[1]/speed)

        #pose[5] += delta[1]/2000
        self.set_realtime_pose(pose=pose)

    def tracking_combine(self, delta):
        print(delta)
        self.reset_error()
        pose = self.get_actual_tcp_pose()
        pose[3] += normeU(delta[0])*(156/220) * norme(delta[0]/3000)  
        pose[4] += normeU(delta[0])           * norme(delta[0]/3000)
        pose[5] -= normeU(delta[0])           * norme(delta[0]/3000)

        pose[3] -= normeU(delta[1])           * norme(delta[1]/3000)  
        pose[4] += normeU(delta[1])           * norme(delta[1]/3000)
        pose[5] += normeU(delta[1]) *(156/220)* norme(delta[1]/3000)
        pose[1] -= delta[0]/10000
        pose[2] -= delta[1]/10000
        self.set_realtime_pose(pose=pose)


    def tracking_combine_bis(self, delta):
        print("BBBB")
        print(delta)
        self.reset_error()
        pose = self.get_actual_tcp_pose()
        pose[4] += delta[0]/3000
        pose[5] += delta[1]/3000
        pose[1] -= delta[0]/20000
        pose[2] -= delta[1]/20000
        self.set_realtime_pose(pose=pose)



#robot.slide()

