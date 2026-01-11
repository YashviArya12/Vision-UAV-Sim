import pybullet as p
import pybullet_data
import time

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #tells pybullet where to look for common files 
p.setGravity(0, 0, -9.81)
p.loadURDF("plane.urdf")
while True:          #loop for live, continuous simulation
    p.stepSimulation()  #moves the world forward by one-step time
    time.sleep(1./240.)    #240 steps per second
