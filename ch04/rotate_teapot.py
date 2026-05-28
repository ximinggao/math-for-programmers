from vectors import to_polar, to_cartesian
from draw_model import draw_model
from teapot import load_triangles
from math import pi


def rotate2d(angle, vector):
    length, a = to_polar(vector)
    return to_cartesian((length, a + angle))


def rotate_z(angle, vector):
    x, y, z = vector
    new_x, new_y = rotate2d(angle, (x, y))
    return new_x, new_y, z


def rotate_z_by(angle):
    def new_function(vector):
        return rotate_z(angle, vector)

    return new_function


def polygon_map(transformation, polygons):
    return [[transformation(vertex) for vertex in triangle] for triangle in polygons]


draw_model(polygon_map(rotate_z_by(pi / 4.0), load_triangles()))
