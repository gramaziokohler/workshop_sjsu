import math
import Rhino.Geometry as rg
from compas_fab.utilities import map_range


def cartesian_to_polar(x, y):
    rho = math.sqrt(x**2 + y**2)
    phi = math.atan2(y, x)
    return(rho, phi)
    
def map2sphere(sphere, circle, points2d, scale):
    points3d = []
    for pt2d in points2d:
        rho, phi = cartesian_to_polar(pt2d.X, pt2d.Y)
        crv = sphere.IsoCurve(1, phi)
        rho_mapped = map_range(rho, 0, circle.Radius, -math.pi/2, math.pi/2 - scale)
        pt3d = crv.PointAt(rho_mapped)
        points3d.append(pt3d)
    return points3d