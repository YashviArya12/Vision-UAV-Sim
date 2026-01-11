from Simulation.environment import Environment
from Simulation.uav import UAV

env = Environment()
uav = UAV()

while True:
    env.step()
    print(uav.get_position())

