#!/usr/bin/python3
import rospy
import numpy as np
import matplotlib.pyplot as plt
from geometry_msgs.msg import Twist

rospy.init_node("turtlesim", anonymous=True)
pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

x1=0
y1=0
theta1=0*np.pi/180
x2=4.0
y2=3
theta2=55*np.pi/180
amax=0.5
Vmax=3

A  = np.array([ [1, x1, x1**2, x1**3],
                [1, x2, x2**2, x2**3],
                [0, 1,   2*x1, 3*x1**2],
                [0, 1,   2*x2, 3*x2**2]
                ])

b = np.array([ [y1],
               [y2],
               [np.tan(theta1)],
               [np.tan(theta2)],               
               ])

a_coef = np.linalg.inv(A) @ b

a0 = a_coef[0];
a1 = a_coef[1];
a2 = a_coef[2];
a3 = a_coef[3];

X = np.linspace(x1, x2, 1000, endpoint= True);
Y = a3 * X**3 +  a2 * X**2 + a1*X + a0

#plt.clf()
#plt.plot(X,Y)
#plt.show()

S = np.linspace(0,0, X.size) 
S[0] = 0
for i in range(1, X.size):
    dX = X[i] - X[i-1]
    dY = Y[i] - Y[i-1]
    dS = np.sqrt( dX**2 + dY**2)
    S[i] = S[i-1] + dS
rospy.loginfo(S[-1])

def parametrize(amax, Vmax, S):
    D = S[-1]
    t1 = Vmax / amax
    tf = D/Vmax + t1
    
    S1 = 0.5*amax*t1**2
    S2 = D - S1
    S3 = D
    
    T = np.linspace(0,0, S.size)
    for i in range(S.size):
        s = S[i]
        if s <= S1:
            T[i] = np.sqrt( 2 * s / amax)
            
        elif s > S1 and s <= S2:
            T[i] = t1 + (s-S1)/Vmax
            
        elif s > S2 and s <= S3:
            T[i] = tf - np.sqrt(2*(D-s)/amax)
    
    return T
T=parametrize(amax,Vmax,S)
#plt.clf()
#plt.plot(T,S)
#plt.show()

def trapvel(amax, Vmax, D, T):
    t1 = Vmax / amax
    tf = D /Vmax + t1
    
    V = np.linspace(0,0, T.size)
    for i in range(T.size):
        t = T[i]
        if t <= t1:
            V[i] = amax*t
            
        elif t > t1 and t <= tf - t1:
            V[i] = Vmax
            
        elif t > (tf-t1) and t <= tf:
            V[i] = Vmax - amax*(t-tf + t1)
            
        else:
            V[i] = 0
            
    return V
V = trapvel(amax,Vmax,S[-1],T)

#plt.clf()
#plt.plot(T,V)
#plt.show()

Q = np.linspace(0,0, T.size)
W = np.linspace(0,0, T.size)
Q[0] = theta1
W[0] = 0
for i in range(1, X.size):
    dY = Y[i] - Y[i-1]
    dX = X[i] - X[i-1]
    Q[i] = np.arctan2(dY, dX)
    W[i] = (Q[i] - Q[i-1]) / (T[i] - T[i-1]) 

#plt.clf()
#plt.plot(T,Q)
#plt.show()

rate = 50
rate1 = rospy.Rate(50)
time_step = 1/rate
T_cmd = np.arange(0, T[-1], time_step)
from scipy.interpolate import interp1d
V_of_t = interp1d(T, V, kind='cubic')
W_of_t = interp1d(T, W, kind='cubic')

V_cmd = V_of_t(T_cmd)
W_cmd = W_of_t(T_cmd)

command = Twist()

i=0
while not rospy.is_shutdown(): 
    if (i<T_cmd.size):
        command.linear.x = V_cmd[i]
        command.linear.y = 0
        command.linear.z = 0
        command.angular.x = 0
        command.angular.y = 0
        command.angular.z = W_cmd[i]
        i=i+1
    else:
        command.linear.x = 0
        command.linear.y = 0
        command.linear.z = 0
        command.angular.x = 0
        command.angular.y = 0
        command.angular.z = 0
    
    pub.publish(command)
    rate1.sleep()