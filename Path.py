#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

# Target poses

x1 = 20;
y1 = 30;
thet1 = 40 * np.pi / 180;

#TO

x2= 80;
y2= 40;
thet2 = 60 * np.pi / 180;


A  = np.array([ [1, x1, x1**2, x1**3],
                [1, x2, x2**2, x2**3],
                [0, 1,   2*x1, 3*x1**2],
                [0, 1,   2*x2, 3*x2**2]
                ])

b = np.array([ [y1],
               [y2],
               [np.tan(thet1)],
               [np.tan(thet2)],               
               ])

a_coef = np.linalg.inv(A) @ b

a0 = a_coef[0];
a1 = a_coef[1];
a2 = a_coef[2];
a3 = a_coef[3];

# Path
X = np.linspace(x1, x2, 1000, endpoint= True);
Y = a3 * X**3 +  a2 * X**2 + a1*X + a0
plt.plot(X,Y)