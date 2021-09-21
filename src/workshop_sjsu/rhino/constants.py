import Rhino.Geometry as rg
import math

RADIUS = 0.2
sphere = rg.Sphere(rg.Point3d(0,0,0), RADIUS)
angle = 0.5 * math.pi
T = rg.Transform.Rotation(angle, rg.Vector3d.YAxis, sphere.Center)
sphere.Transform(T)