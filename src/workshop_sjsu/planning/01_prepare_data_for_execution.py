# 1. Move points to sphere center and make frames
# 2. Reduce to only use buildable
# 3. Create paths in between with "off light"

from workshop_sjsu.reachability.setup import Client
from workshop_sjsu.reachability.setup import sjsu_setup
from workshop_sjsu import DATA
import os
import compas

from compas.geometry import Point, Plane, Frame

from compas.geometry import Vector
from compas.geometry import closest_point_on_plane
from compas_fab.backends.pybullet import LOG

import logging
LOG.setLevel(logging.ERROR)


NAME = "example03"
SPHERE_CENTER = Point(0.407143, 0, 0.226667)
UP_PLANE = Plane((0.407143, 0, 0.347788), (0, 0, 1))

IK_IDX = 2


def translate_and_create_frames(points3d):
    frames = []
    for points_per_path in points3d:
        frames.append([])
        for point in points_per_path:
            point = Point(*point) + Vector(*SPHERE_CENTER)
            normal = point - SPHERE_CENTER
            plane = Plane(point, normal)
            frame = Frame.from_plane(plane)
            frames[-1].append(frame)
    return frames


def reduce_to_reachable(frames, connection_type='gui'):

    configurations = []
    indices2keep = []

    with Client(connection_type=connection_type) as client:

        robot, _ = sjsu_setup(client)

        num_frames = sum([len(frames_per_path) for frames_per_path in frames])

        for i, frames_per_path in enumerate(frames):

            configurations_per_path = []
            for frame_tcf in frames_per_path:
                frame0_t0cf = robot.attached_tool.from_tcf_to_t0cf([frame_tcf])[
                    0]
                try:
                    configs = client.inverse_kinematics(robot, frame0_t0cf, options={
                                                        "check_collision": True, "cull": False})
                    solution = configs[IK_IDX]
                except ValueError:
                    solution = None
                if not solution:
                    break
                else:
                    configurations_per_path.append(solution)
            else:
                configurations.append(configurations_per_path)
                indices2keep.append(i)

        num_configurations = sum([len(configurations_per_path)
                                 for configurations_per_path in configurations])
        print("Removing %i of %i frames, since they are not reachable." %
              (num_frames - num_configurations, num_frames))

    return configurations, indices2keep


def add_transition_between_paths_and_flatten(frames, gradients, colors, configurations, connection_type='gui'):

    frames_flattened = []
    gradients_flattened = []
    colors_flattened = []
    configurations_flattened = []

    print(len(frames))
    print(len(frames[0]))
    print()

    with Client(connection_type=connection_type) as client:
        robot, _ = sjsu_setup(client)

        for i, (path1, path2) in enumerate(zip(frames[:-1], frames[1:])):

            # add another 2
            point_s = closest_point_on_plane(path1[-1].point, UP_PLANE)
            frame_s = Frame(point_s, path1[-1].xaxis, path1[-1].yaxis)

            point_e = closest_point_on_plane(path2[0].point, UP_PLANE)
            frame_e = Frame(point_e, path2[-1].xaxis, path2[-1].yaxis)

            if i == 0:
                frames_flattened += path1
                gradients_flattened += gradients[i]
                colors_flattened += colors[i]
                configurations_flattened += configurations[i]

            # transition
            frames_flattened += [frame_s, frame_e]
            gradients_flattened += [0, 0]
            colors_flattened += [colors[i][-1], colors[i + 1][0]]

            if i == 0:
                print(gradients_flattened)

            # configurations_flattened
            for frame_tcf in [frame_s, frame_e]:
                frame0_t0cf = robot.attached_tool.from_tcf_to_t0cf([frame_tcf])[
                    0]
                configs = client.inverse_kinematics(robot, frame0_t0cf, options={
                                                    "check_collision": True, "cull": False})
                solution = configs[IK_IDX]
                configurations_flattened.append(solution)

            # path2
            frames_flattened += path2
            gradients_flattened += gradients[i + 1]
            colors_flattened += colors[i + 1]
            configurations_flattened += configurations[i + 1]

    return frames_flattened, gradients_flattened, colors_flattened, configurations_flattened


if __name__ == "__main__":
    filepath = os.path.join(DATA, "%s.json" % NAME)

    data = compas.json_load(filepath)

    gradients = data['gradients']
    points3d = data['points3d']
    colors = data['colors']

    # 1. Move points to defined sphere center (in RCF) and make frames
    frames = translate_and_create_frames(points3d)

    # 2. Reduce to only use buildable paths
    ct = 'gui'
    # ct = 'direct'
    configurations, indices2keep = reduce_to_reachable(
        frames, connection_type=ct)

    # remove also from frames, gradients and colors
    frames = [frames[i] for i in indices2keep]
    gradients = [gradients[i] for i in indices2keep]
    colors = [colors[i] for i in indices2keep]

    F, G, C, J = add_transition_between_paths_and_flatten(
        frames, gradients, colors, configurations, connection_type='gui')

    data = {}
    data['frames'] = F
    data['gradients'] = G
    data['colors'] = C
    data['configurations'] = J

    filepath = os.path.join(DATA, "%s_execution.json" % NAME)
    compas.json_dump(data, filepath)
