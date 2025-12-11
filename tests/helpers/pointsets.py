"""Small reusable pointsets for tests."""

def triangle():
    """Return a simple 3-point triangle."""
    return [(0.0, 0.0), (1.0, 0.0), (0.0, 1.0)]


def square_ccw():
    """Return a square in counter-clockwise order."""
    return [(0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0)]


def colinear_line(n=4):
    """Return n colinear points along the x-axis."""
    return [(float(i), 0.0) for i in range(n)]

def duplicate_points():
    """Return a pointset with duplicate points."""
    return [(0.0, 0.0), (1.0, 0.0), (1.0, 0.0), (0.0, 1.0), (0.0, 1.0)]

def polygon_convex(n=5, radius=1.0):
    """Generate a convex polygon with n vertices."""
    from math import cos, pi, sin
    return [
        (radius * cos(2 * pi * i / n), radius * sin(2 * pi * i / n)) for i in range(n)
        ]