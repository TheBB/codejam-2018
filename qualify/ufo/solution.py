from math import sqrt, acos, cos, sin, asin, atan, pi


def low(size):
    angle = pi/4 - acos(size / sqrt(2))

    # Rotate around the z axis
    return [
        (.5 * cos(angle), .5 * sin(angle), 0),
        (-.5 * sin(angle), .5 * cos(angle), 0),
        (0, 0, .5),
    ]


def high(size):
    angle = asin(size / sqrt(3)) - asin(sqrt(2/3))
    z = 1 / 2 / sqrt(2)

    # Rotate around the x axis
    return [
        (z, z * cos(angle), -z * sin(angle)),
        (-z, z * cos(angle), -z * sin(angle)),
        (0, .5 * sin(angle), .5 * cos(angle)),
    ]


if __name__ == '__main__':
    ncases = int(input())
    for i in range(1, ncases + 1):
        size = float(input())
        vecs = (low if size <= sqrt(2) else high)(size)
        print('Case #{}:'.format(i))
        for vec in vecs:
            print(' '.join(str(v) for v in vec))
