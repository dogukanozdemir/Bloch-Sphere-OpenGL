import numpy as np
import math
import cmath
import sys
print(sys.version)

qbit = np.matrix([[1+0j],[0+0j]])
X = np.matrix([[0,1+0j],[1,0]])
Y = np.matrix([[0,-1j],[1j,0]])
I = np.matrix([[1+0j,0],[0,1]]) #Inverse
H = 1/math.sqrt(2) * np.matrix( [[1+0j,1],[1,-1]]) #Hadamard
X = np.matrix([[0,1+0j],[1,0]]) #PauliX
Y = np.matrix([[0,-1j],[1j,0]]) #PauliY
Z = np.matrix([[1+0j,0],[0,-1]]) #PauliZ
S = np.matrix([[1+0j,0],[0,1j]]) #Phase
#T = np.matrix([[1,0],[0,math.exp(1j*(math.pi/4))]]) #PI/8
sN = 1/math.sqrt(2) * np.matrix( [[1+0j,-1],[1,1]]) #Sqrt Not

theta = math.pi / 2
phi = 0

beta = cmath.exp(1j * (phi)) * math.sin(theta / 2)
alpha = math.cos(theta / 2)
print("state vector [" + str(alpha) + "]," + "[" + str(beta) + "]")
print("%" +  str((abs(alpha)**2) * 100))
print((abs(beta)**2) + (abs(alpha)**2))

"""
def xGate(theta,phi):
    theta = math.pi - theta
"""
"""
def yGate(theta,phi):
    if theta != 0 or theta != math.pi:
        phi = (phi + math.pi) % (math.pi * 2)
    theta = math.pi - theta
"""
"""
def zGate(theta,phi):
    if theta != 0 or theta != math.pi:
        phi = (phi + math.pi) % (math.pi * 2)
"""
"""
theta = 90 <-> 90
phi = 90 <-> 270

theta = 45 <-> 45
phi = 0 <-> 0

theta = 135 <-> 45
phi = 0 <-> 180


"""