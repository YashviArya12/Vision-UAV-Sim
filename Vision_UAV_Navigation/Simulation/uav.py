import pybullet as p
import pybullet_data


class UAV:
    def __init__(self, start_position=[0, 0, 1]):
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        self.uav_id = p.loadURDF(
            "drone.urdf",
            start_position
        )

    def get_position(self):
        position, orientation = p.getBasePositionAndOrientation(self.uav_id)
        return position
