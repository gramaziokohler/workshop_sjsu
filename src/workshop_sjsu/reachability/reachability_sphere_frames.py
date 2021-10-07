from workshop_sjsu.reachability.reachability_map import ReachabilityMap


if __name__ == "__main__":

    import os
    import compas

    from compas.geometry import Translation
    from compas.datastructures import Mesh

    from compas_fab.backends import PyBulletClient
    from compas_fab.robots import CollisionMesh
    from compas_fab.robots import PlanningScene

    from workshop_sjsu import DATA
    from workshop_sjsu.ur.kinematics.analytical_inverse_kinematics import UR5AnalyticalIK
    from workshop_sjsu.reachability.setup import setup

    frames = compas.json_load(os.path.join(DATA, "sphere_frames.json"))
    centers = compas.json_load(os.path.join(DATA, "sphere_centers.json"))

    print(len(frames))
    print(len(centers))
    assert(len(frames) == len(centers))

    filename = os.path.join(DATA, "reachability_sphere_frames_04.json")

    class Client(PyBulletClient):
        def inverse_kinematics(self, *args, **kwargs):
            return UR5AnalyticalIK(self)(*args, **kwargs)

    ct = 'gui'
    # ct = 'direct'
    with Client(connection_type=ct) as client:

        robot = setup(client)

        map = ReachabilityMap()

        counter = 0
        for center, frames_per_sphere in zip(centers, frames):

            camera_mesh = Mesh.from_obj(os.path.join(DATA, "camera.obj"))
            camera_mesh.transform(Translation.from_vector(center))

            scene = PlanningScene(robot)
            cm = CollisionMesh(camera_mesh, 'camera')
            scene.add_collision_mesh(cm)

            frames_per_point = []
            configurations_per_point = []

            for i, frame_tcf in enumerate(frames_per_sphere):

                print("Point %i of %i ===============" %
                      (i+1, len(frames_per_sphere)))

                frame0_t0cf = robot.attached_tool.from_tcf_to_t0cf([frame_tcf])[
                    0]
                try:
                    configurations = client.inverse_kinematics(
                        robot, frame0_t0cf, options={"check_collision": True, "cull": False})
                    if len(configurations):
                        frames_per_point.append(frame_tcf)
                        configurations_per_point.append(configurations)
                except ValueError:
                    continue

            map.frames.append(frames_per_point)
            map.configurations.append(configurations_per_point)

        map.to_json(filename)
