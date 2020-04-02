#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 17:01:03 2020

@author: soumik
"""
# A SIR model for the spread of virus

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from pylab import *

N=10000     # Initial population
I=1         # Initially infected people
R=0         # 0 Recovered
S=N-I-R     # Susceptible (N=S+I+R)

radius = 1  # Radius of infection
prob = 0.2  # Probability of Infection
T=14        # Time-play

omega = 1                                               # Rate of social distancing
gamma = .5                                              # Rate of recovery
beta = 2.5           									# Reproduction Number
beta2 = radius*prob*T*(beta/(beta + omega + gamma))     # Rate of infection
    

def SIR(vals,t,b,g):
    S,I,R=vals
    
    dS=-b*S*I/N     # dS/dt
    dI=b*S*I/N - g*I
    dR=g*I
    
    return [dS,dI,dR]

    
t=np.linspace(0,4*T,1000)
x=[S,I,R]           # Initial params
rates=(beta2,gamma)
sol=odeint(SIR,x,t,args=rates)

# Plot ODE solutions
plt.plot(t,sol[:,0])
plt.plot(t,sol[:,1])
plt.plot(t,sol[:,2])

plt.xlabel('Time')
plt.ylabel('Population')
plt.legend(['S','I','R'],shadow=True)
plt.draw()
savefig("/home/soumik/Desktop/covid-19/results/"+"diff_radius"+str(radius)+"_prob"+str(prob)+"_omega"+str(omega)+".png",dpi=400)

