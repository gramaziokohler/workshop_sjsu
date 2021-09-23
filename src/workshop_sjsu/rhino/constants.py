import Rhino.Geometry as rg
import math

RADIUS = 0.15
sphere = rg.Sphere(rg.Point3d(0, 0, 0), RADIUS)
angle = math.pi
T = rg.Transform.Rotation(angle, rg.Vector3d.YAxis, sphere.Center)
sphere.Transform(T)
