"""CIS 376 Project Two - Math Library
Requirements:
    * Data structures
        [x] Vec2 has 3 coordinates (one extra for homogenous coordinate or w value)
        [x] Vec3 has 4 coordinates (one extra for homogenous coordinate or w value)
        [x] 4x4 Matrix
    * Functions
        [x] Calculate the cross product and return a vector
        [x] Calculate the dot product and return the scalar
        [x] Calculate the angle between two vectors
        [x] Add two vectors
        [x] Add two matrices and return a matrix
        [x] Subtract two vectors
        [x] Subtract two matrices and return a matrix
        [x] Multiply a matrix by a matrix and return a matrix
        [x] Multiply a vector by a matrix and return a vector
        [x] Normalize a vector
        [x] Find the magnitude of a vector
            * One that returns the square root of the magnitude
            * One that returns the value with no square root applied
        [x] Determine if two vectors are the same (have the same values)
        [x] Determine if two matrices are the same (have the same values) 
        
Foreword:
    I wanted to acknowledge that there are a number of things here that 
    could have been done differently and way more concisely. I settled
    on the heavy-handed "explicitly define each function" approach rather
    than a sleeker "computer sciency" approach because the main
    point of this exercise is to learn more about these math principles, 
    not to write a super nice math library. If this were a library which 
    I needed to use for the remainder of the class, then I probably would 
    have been more elegant in the structure of everything here. 
"""

import math


def vec2_normalize(v0):
    """returns the normalized version of vector v0"""
    mag = vec2_mag(v0)
    n_x = v0.x / mag
    n_y = v0.y / mag
    return Vec2(n_x, n_y, v0.w)


def vec3_normalize(v0):
    """returns the normalized version of vector v0"""
    mag = vec3_mag(v0)
    n_x = v0.x / mag
    n_y = v0.y / mag
    n_z = v0.z / mag
    return Vec3(n_x, n_y, n_z, v0.w)


def vec2_compare(v0, v1):
    """Determines if two vectors are the same"""
    if v0.x == v1.x and v0.y == v1.y and v0.w == v1.w:
        return True
    return False


def vec3_compare(v0, v1):
    """Determines if two vectors are the same"""
    if v0.x == v1.x and v0.y == v1.y and v0.z == v1.z and v0.w == v1.w:
        return True
    return False


def vec2_cross(v0, v1):
    """Calculates the cross product and returns a vector"""
    return v0.x*v1.y - v0.y*v1.x


def vec3_cross(v0, v1):
    """Calculates the cross product and returns a vector"""
    return Vec3(v0.y*v1.z - v0.z*v1.y, v0.z*v1.x - v0.x*v1.z, v0.x*v1.y - v0.y*v1.x, 1)


def vec2_dot(v0, v1):
    """Calculates the dot product and returns the scalar"""
    return v0.x * v1.x + v0.y * v1.y


def vec3_dot(v0, v1):
    """Calculates the dot product and returns the scalar"""
    return v0.x * v1.x + v0.y * v1.y + v0.z * v1.z


def vec2_angle(v0, v1):
    """Calculates the angle between two vectors"""
    dot = vec2_dot(v0, v1)
    v0_mag = vec2_mag(v0)
    v1_mag = vec2_mag(v1)
    angle = math.acos(dot/(v0_mag*v1_mag))
    return angle


def vec3_angle(v0, v1):
    """Calculates the angle between two vectors"""
    dot = vec3_dot(v0, v1)
    v0_mag = vec3_mag(v0)
    v1_mag = vec3_mag(v1)
    angle = math.acos(dot/(v0_mag*v1_mag))
    return angle


def vec2_mag(v0):
    """Find the magnitude of a vector and returns the square root of the magnitude"""
    return math.sqrt(vec2_mag_cmp(v0))


def vec3_mag(v0):
    """Find the magnitude of a vector and returns the square root of the magnitude"""
    return math.sqrt(vec3_mag_cmp(v0))


def vec2_mag_cmp(v0):
    """Find the magnitude of a vector and returns the value with no square root applied"""
    return v0.x**2 + v0.y**2


def vec3_mag_cmp(v0):
    """Find the magnitude of a vector and returns the value with no square root applied"""
    return v0.x**2 + v0.y**2 + v0.z**2


def vec2_add(v0, v1):
    """Adds two vectors"""
    return Vec2(v0.x + v1.x, v0.y + v1.y, 1)


def vec3_add(v0, v1):
    """Adds two vectors"""
    return Vec3(v0.x + v1.x, v0.y + v1.y, v0.z + v1.z, 1)


def vec2_sub(v0, v1):
    """Subtracts two vectors"""
    return Vec2(v0.x - v1.x, v0.y - v1.y, 1)


def vec3_sub(v0, v1):
    """Subtracts two vectors"""
    return Vec3(v0.x - v1.x, v0.y - v1.y, v0.z - v1.z, 1)


def matrix4_add(m0, m1):
    """Adds two matrices and returns a matrix"""
    r0 = (m0.r0[0] + m1.r0[0], m0.r0[1] + m1.r0[1], m0.r0[2] + m1.r0[2], m0.r0[3] + m1.r0[3])
    r1 = (m0.r1[0] + m1.r1[0], m0.r1[1] + m1.r1[1], m0.r1[2] + m1.r1[2], m0.r1[3] + m1.r1[3])
    r2 = (m0.r2[0] + m1.r2[0], m0.r2[1] + m1.r2[1], m0.r2[2] + m1.r2[2], m0.r2[3] + m1.r2[3])
    r3 = (m0.r3[0] + m1.r3[0], m0.r3[1] + m1.r3[1], m0.r3[2] + m1.r3[2], m0.r3[3] + m1.r3[3])
    return Matrix4([r0, r1, r2, r3])


def matrix4_sub(m0, m1):
    """Subtracts two matrices and returns a matrix"""
    r0 = (m0.r0[0] - m1.r0[0], m0.r0[1] - m1.r0[1], m0.r0[2] - m1.r0[2], m0.r0[3] - m1.r0[3])
    r1 = (m0.r1[0] - m1.r1[0], m0.r1[1] - m1.r1[1], m0.r1[2] - m1.r1[2], m0.r1[3] - m1.r1[3])
    r2 = (m0.r2[0] - m1.r2[0], m0.r2[1] - m1.r2[1], m0.r2[2] - m1.r2[2], m0.r2[3] - m1.r2[3])
    r3 = (m0.r3[0] - m1.r3[0], m0.r3[1] - m1.r3[1], m0.r3[2] - m1.r3[2], m0.r3[3] - m1.r3[3])
    return Matrix4([r0, r1, r2, r3])


def matrix4_mm_mult(m0, m1):
    """Multiplies a matrix by a matrix and returns a matrix"""
    r0 = (m0.r0[0] * m1.r0[0] + m0.r0[1] * m1.r1[0] + m0.r0[2] * m1.r2[0] + m0.r0[3] * m1.r3[0],
          m0.r0[0] * m1.r0[1] + m0.r0[1] * m1.r1[1] + m0.r0[2] * m1.r2[1] + m0.r0[3] * m1.r3[1],
          m0.r0[0] * m1.r0[2] + m0.r0[1] * m1.r1[2] + m0.r0[2] * m1.r2[2] + m0.r0[3] * m1.r3[2],
          m0.r0[0] * m1.r0[3] + m0.r0[1] * m1.r1[3] + m0.r0[2] * m1.r2[3] + m0.r0[3] * m1.r3[3])

    r1 = (m0.r1[0] * m1.r0[0] + m0.r1[1] * m1.r1[0] + m0.r1[2] * m1.r2[0] + m0.r1[3] * m1.r3[0],
          m0.r1[0] * m1.r0[1] + m0.r1[1] * m1.r1[1] + m0.r1[2] * m1.r2[1] + m0.r1[3] * m1.r3[1],
          m0.r1[0] * m1.r0[2] + m0.r1[1] * m1.r1[2] + m0.r1[2] * m1.r2[2] + m0.r1[3] * m1.r3[2],
          m0.r1[0] * m1.r0[3] + m0.r1[1] * m1.r1[3] + m0.r1[2] * m1.r2[3] + m0.r1[3] * m1.r3[3])

    r2 = (m0.r2[0] * m1.r0[0] + m0.r2[1] * m1.r1[0] + m0.r2[2] * m1.r2[0] + m0.r2[3] * m1.r3[0],
          m0.r2[0] * m1.r0[1] + m0.r2[1] * m1.r1[1] + m0.r2[2] * m1.r2[1] + m0.r2[3] * m1.r3[1],
          m0.r2[0] * m1.r0[2] + m0.r2[1] * m1.r1[2] + m0.r2[2] * m1.r2[2] + m0.r2[3] * m1.r3[2],
          m0.r2[0] * m1.r0[3] + m0.r2[1] * m1.r1[3] + m0.r2[2] * m1.r2[3] + m0.r2[3] * m1.r3[3])

    r3 = (m0.r3[0] * m1.r0[0] + m0.r3[1] * m1.r1[0] + m0.r3[2] * m1.r2[0] + m0.r3[3] * m1.r3[0],
          m0.r3[0] * m1.r0[1] + m0.r3[1] * m1.r1[1] + m0.r3[2] * m1.r2[1] + m0.r3[3] * m1.r3[1],
          m0.r3[0] * m1.r0[2] + m0.r3[1] * m1.r1[2] + m0.r3[2] * m1.r2[2] + m0.r3[3] * m1.r3[2],
          m0.r3[0] * m1.r0[3] + m0.r3[1] * m1.r1[3] + m0.r3[2] * m1.r2[3] + m0.r3[3] * m1.r3[3])
    return Matrix4([r0, r1, r2, r3])


def matrix4_mv_mult(m0, v0):
    """Multiplies a vector by a matrix and returns a vector"""
    x = (m0.r0[0] * v0.x + m0.r0[1] * v0.y + m0.r0[2] * v0.z + m0.r0[3] * v0.w)
    y = (m0.r1[0] * v0.x + m0.r1[1] * v0.y + m0.r1[2] * v0.z + m0.r1[3] * v0.w)
    z = (m0.r2[0] * v0.x + m0.r2[1] * v0.y + m0.r2[2] * v0.z + m0.r2[3] * v0.w)
    w = (m0.r3[0] * v0.x + m0.r3[1] * v0.y + m0.r3[2] * v0.z + m0.r3[3] * v0.w)
    return Vec3(x, y, z, w)


def matrix4_comp(m0, m1):
    """Determines if two matrices are the same"""
    if m0.r0 != m1.r0 or m0.r1 != m1.r1 or m0.r2 != m1.r2 or m0.r3 != m1.r3:
        return False
    return True


class Matrix4:
    """Represents a 4x4 matrix

        Attributes:
            m: a list of four tuples of length 4
    """

    def __init__(self, m: list):
        # Ensure matrix is of correct dimensions
        if len(m) < 0 or len(m) > 4:
            raise ValueError(f"Incorrect amount of rows. Row count should be 4, but it is {len(m)}.")

        for r in m:
            if len(r) < 0 or len(r) > 4:
                print("NO")
                raise ValueError(f"Row length should be 4, but it is {len(m)}.")

        self.r0 = m[0]
        self.r1 = m[1]
        self.r2 = m[2]
        self.r3 = m[3]

    def __str__(self):
        return f"Matrix4:\n" \
               f"[{self.r0[0]:3} {self.r0[1]:3} {self.r0[2]:3} {self.r0[3]:3} ]\n" \
               f"[{self.r1[0]:3} {self.r1[1]:3} {self.r1[2]:3} {self.r1[3]:3} ]\n" \
               f"[{self.r2[0]:3} {self.r2[1]:3} {self.r2[2]:3} {self.r2[3]:3} ]\n" \
               f"[{self.r3[0]:3} {self.r3[1]:3} {self.r3[2]:3} {self.r3[3]:3} ]"


class Vec2:
    """Represents a 4x4 matrix

            Attributes:
                x, y: the first and second elements of the vector
                w: the third element of the vector, used as the homogenous coordinate
    """

    def __init__(self, x, y, w):
        self.x = x
        self.y = y
        self.w = w

    def __str__(self):
        return f"Vec2:\n" \
               f"<{self.x:3} {self.y:3} {self.w:3} >"


# W for homogenous coordinate, 0 if vector, 1 if point
class Vec3:
    """Represents a 4x4 matrix

                Attributes:
                    x, y, z: the first, second, and third elements of the vector
                    w: the fourth element of the vector, used as the homogenous coordinate
    """

    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __str__(self):
        return f"Vec2:\n" \
               f"<{self.x:3} {self.y:3} {self.z:3} {self.w:3} >"
