import pybullet as p
import pybullet_data
import time

class Environment:
    def __init__(self):
        p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())  #tells pybullet where to find built-in models
        p.setGravity(0, 0, -9.81)
        p.loadURDF("plane.urdf")

    def step(self):
        p.stepSimulation()  #computes the next state based on current forces/constraints 
        time.sleep(1.0 / 240.0)  #240 steps per second, for smooth running of simulation 
