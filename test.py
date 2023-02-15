import mathlib as ml


def test():
    v0 = ml.Vec3(1, 1, 1, 1)

    m0 = ml.Matrix4([
        (0,  1,  2,  3),
        (4,  5,  6,  7),
        (8,  9,  10, 11),
        (12, 13, 14, 15)
    ])
    m1 = ml.Matrix4([
        (15, 14, 13, 12),
        (11, 10, 9,  8),
        (7,  6,  5,  4),
        (3,  2,  1,  0)
    ])

    print(ml.matrix4_comp(m0, m0))
    print(ml.matrix4_comp(m0, m1))

    # m3 = ml.matrix4_mv_mult(m0, v0)
    # print(v0)
    # print(m0)
    # print(m3)


if __name__ == '__main__':
    test()
