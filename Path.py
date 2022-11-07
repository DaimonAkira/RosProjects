# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 16:21:53 2022

@author: Akira
"""

import numpy as np
import

x1 = 20;
y1 = 30;
q1 = 10 * np.pi / 180;

x2 = 60;
y2 = 75;
q2 = 60 * np.pi / 180;


A = np.array([ [1,x1,x1**2,x1**3],
               [1,x2,x2**2,x2**3],
               [0,1,2*x1,3*x1**2],
               [0,1,2*x2,3*x2**2]    
            ])

b = np.array([  [y1],
                [y2],
                [tan(q1)],
                [tan(q2)]   
            ])