"""Small reusable pointsets for tests."""

def triangle():
    return [(0.0, 0.0), (1.0, 0.0), (0.0, 1.0)]


def square_ccw():
    return [(0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0)]


def colinear_line(n=4):
    return [(float(i), 0.0) for i in range(n)]

def duplicate_points():
    return [(0.0, 0.0), (1.0, 0.0), (1.0, 0.0), (0.0, 1.0), (0.0, 1.0)]

def polygon_convex(n=5, radius=1.0):
    """Generate a convex polygon with n vertices."""
    from math import cos, sin, pi
    return [(radius * cos(2 * pi * i / n), radius * sin(2 * pi * i / n)) for i in range(n)]