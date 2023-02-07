import math

"""CIS 376 Project Two - Math Library
Requirements:
    * Data structures
        [ ] Vec2 has 3 coordinates (one extra for homogenous coordinate or w value)
        [ ] Vec3 has 4 coordinates (one extra for homogenous coordinate or w value)
        [ ] 4x4 Matrix
    * Functions
        [ ] Calculate the cross product and return a vector
        [ ] Calculate the dot product and return the scalar
        [ ] Calculate the angle between two vectors
        [ ] Add two vectors
        [ ] Add two matrices and return a matrix
        [ ] Subtract two vectors
        [ ] Subtract two matrices and return a matrix
        [ ] Multiply a matrix by a matrix and return a matrix
        [ ] Multiply a vector by a matrix and return a vector
        [ ] Normalize a vector
        [ ] Find the magnitude of a vector
            * One that returns the square root of the magnitude
            * One that returns the value with no square root applied
        [ ] Determine if two vectors are the same (have the same values)
        [ ] Determine if two matrices are the same (have the same values)
"""


def vec2_cross(v0, v1):
    return v0.x*v1.y - v0.y*v1.x


def vec3_cross(v0, v1):
    return Vec3(v0.y*v1.z - v0.z*v1.y, v0.z*v1.x - v0.x*v1.z, v0.x*v1.y - v0.y*v1.x, 1)


def vec2_dot(v0, v1):
    return v0.x * v1.x + v0.y * v1.y


def vec3_dot(v0, v1):
    return v0.x * v1.x + v0.y * v1.y + v0.z * v1.z


def vec2_angle(v0, v1):
    dot = vec2_dot(v0, v1)
    v0_mag = vec2_mag(v0)
    v1_mag = vec2_mag(v1)
    angle = math.acos(dot/(v0_mag*v1_mag))
    return angle


def vec3_angle(v0, v1):
    dot = vec3_dot(v0, v1)
    v0_mag = vec3_mag(v0)
    v1_mag = vec3_mag(v1)
    angle = math.acos(dot/(v0_mag*v1_mag))
    return angle


def vec2_mag(v0):
    return math.sqrt(vec2_mag_cmp(v0))


def vec3_mag(v0):
    return math.sqrt(vec3_mag_cmp(v0))


def vec2_mag_cmp(v0):
    return pow(v0.x, 2) + pow(v0.y, 2)


def vec3_mag_cmp(v0):
    return pow(v0.x, 2) + pow(v0.y, 2) + pow(v0.z, 2)


def vec2_add(v0, v1):
    return Vec2(v0.x + v1.x, v0.y + v1.y, 1)


def vec3_add(v0, v1):
    return Vec3(v0.x + v1.x, v0.y + v1.y, v0.z + v1.z, 1)


def vec2_sub(v0, v1):
    return Vec2(v0.x - v1.x, v0.y - v1.y, 1)


def vec3_sub(v0, v1):
    return Vec3(v0.x - v1.x, v0.y - v1.y, v0.z - v1.z, 1)


class Vec2:
    def __init__(self, x, y, w):
        self.x = x
        self.y = y
        self.w = w

    def __str__(self):
        return "Vec2: <{0}, {1}, {2}, {3} >".format(self.x, self.y, self.z, self.w)


# W for homogenous coordinate, 0 if vector, 1 if point
class Vec3:
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __str__(self):
        return "Vec3: <{0}, {1}, {2}, {3} >".format(self.x, self.y, self.z, self.w)

