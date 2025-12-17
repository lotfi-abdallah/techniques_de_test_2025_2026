Module tp1.triangulator
=======================
Simple triangulation utilities.

This provides a minimal triangulation implementation sufficient for the
test-first workflow: it removes duplicate points, checks for trivial cases
and uses a fan triangulation for convex polygons (and as a fallback).

The goal here is to provide a working, predictable implementation that can
be extended later to a full Delaunay or ear-clipping algorithm.

Functions
---------

`fan_triangulate(n: int) ‑> list[tuple[int, int, int]]`
:   Compute fan triangulation from vertex 0 for n points.

`triangulate(points: list[tuple[float, float]]) ‑> list[tuple[int, int, int]]`
:   Compute a list of triangles (by vertex indices) from `points`.
    
    Returns an empty list when triangulation is impossible (too few points,
    collinear points, ...). The implementation is intentionally simple: for
    convex polygons it produces a fan triangulation; otherwise it falls back
    to the same fan strategy after removing duplicates.

Classes
-------

`TriangulationError(*args, **kwargs)`
:   Raised when triangulation computation fails.

    ### Ancestors (in MRO)

    * builtins.Exception
    * builtins.BaseException