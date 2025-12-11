"""Simple triangulation utilities.

This provides a minimal triangulation implementation sufficient for the
test-first workflow: it removes duplicate points, checks for trivial cases
and uses a fan triangulation for convex polygons (and as a fallback).

The goal here is to provide a working, predictable implementation that can
be extended later to a full Delaunay or ear-clipping algorithm.
"""

Point = tuple[float, float]
Triangle = tuple[int, int, int]


class TriangulationError(Exception):
    pass


def _cross(o: Point, a: Point, b: Point) -> float:
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def _remove_duplicates(points: list[Point]) -> list[Point]:
    seen = set()
    out = []
    for p in points:
        key = (p[0], p[1])
        if key in seen:
            continue
        seen.add(key)
        out.append(p)
    return out


def _is_collinear(points: list[Point], eps: float = 1e-9) -> bool:
    if len(points) < 3:
        return True
    # find two distinct points
    a = None
    b = None
    for p in points:
        if a is None:
            a = p
            continue
        if p != a:
            b = p
            break
    if b is None:
        return True
    return all(abs(_cross(a, b, p)) <= eps for p in points)
    # for p in points:
    #     if abs(_cross(a, b, p)) > eps:
    #         return False
    # return True


def _is_convex_polygon(points: list[Point]) -> bool:
    n = len(points)
    if n < 3:
        return False
    signs = []
    for i in range(n):
        o = points[i]
        a = points[(i + 1) % n]
        b = points[(i + 2) % n]
        c = _cross(o, a, b)
        if abs(c) < 1e-12:
            continue
        signs.append(c > 0)
    return all(s == signs[0] for s in signs) if signs else False

def triangulate(points: list[Point]) -> list[Triangle]:
    """Compute a list of triangles (by vertex indices) from `points`.

    Returns an empty list when triangulation is impossible (too few points,
    collinear points, ...). The implementation is intentionally simple: for
    convex polygons it produces a fan triangulation; otherwise it falls back
    to the same fan strategy after removing duplicates.
    """
    pts = _remove_duplicates(points)
    n = len(pts)
    if n < 3:
        return []
    if _is_collinear(pts):
        return []
    if n == 3:
        return [(0, 1, 2)]

    # If the input looks like a convex polygon, a fan triangulation is valid
    if _is_convex_polygon(pts):
        return fan_triangulate(n)

    # Fallback: use a fan triangulation anyway (works for many simple cases)
    try:
        return fan_triangulate(n)
    except Exception as exc:  # pragma: no cover - defensive
        raise TriangulationError("Triangulation failed") from exc

def fan_triangulate(n: int) -> list[Triangle]:
    return [(0, i, i + 1) for i in range(1, n - 1)]