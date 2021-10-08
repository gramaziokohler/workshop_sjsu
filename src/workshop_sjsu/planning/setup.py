import os
import compas_fab
from compas_fab.robots import Tool
from compas_fab.robots import RobotSemantics
from compas_fab.robots import PlanningScene
from compas_fab.robots import CollisionMesh
from compas_fab.backends import PyBulletClient
from compas.datastructures import Mesh

from workshop_sjsu import DATA
from workshop_sjsu.ur.kinematics.analytical_inverse_kinematics import UR5AnalyticalIK


def sjsu_setup(client):
    tool = Tool.from_json(os.path.join(DATA, "tool.json"))

    urdf_filename = compas_fab.get(
        'universal_robot/ur_description/urdf/ur5.urdf')
    srdf_filename = compas_fab.get(
        'universal_robot/ur5_moveit_config/config/ur5.srdf')

    # TODO: convert to pybullet convex meshes?

    # Load UR5
    robot = client.load_robot(urdf_filename)
    robot.semantics = RobotSemantics.from_srdf_file(srdf_filename, robot.model)

    # Update disabled collisions
    client.disabled_collisions = robot.semantics.disabled_collisions

    # Attach tool and convert frames
    robot.attach_tool(tool)
    scene = PlanningScene(robot)

    camera_mesh = Mesh.from_json(os.path.join(DATA, "camera_in_position.json"))
    cm = CollisionMesh(camera_mesh, 'camera')
    scene.add_collision_mesh(cm)

    return robot, scene


class Client(PyBulletClient):
    def inverse_kinematics(self, *args, **kwargs):
        return UR5AnalyticalIK(self)(*args, **kwargs)