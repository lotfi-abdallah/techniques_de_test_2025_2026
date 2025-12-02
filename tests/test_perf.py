import sys
import time
import random
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

import pytest

import triangulator
from utils.to_binary_string import to_binary_string, to_lists


@pytest.mark.perf
def test_triangulation_large_random():
    """Measure triangulation speed on a moderately large random pointset.

    This test is marked `perf` so it can be excluded from normal test runs.
    It asserts the operation completes (no strict microsecond limits).
    """
    random.seed(0)
    n = 100000
    points = [(random.random() * 1000.0, random.random() * 1000.0) for _ in range(n)]

    start = time.perf_counter()
    tris = triangulator.triangulate(points)
    duration = time.perf_counter() - start

    print(f"triangulation: {n} points -> {len(tris)} triangles in {duration:.3f}s")
    assert isinstance(tris, list)
    # soft upper bound to avoid pathological hangs on CI
    assert duration < 1


@pytest.mark.perf
def test_serialization_roundtrip_large():
    """Measure serialization/deserialization throughput for a large pointset."""
    n = 100000
    points = [(float(i), float((i * 3) % 1000)) for i in range(n)]
    triangles = []

    start = time.perf_counter()
    data = to_binary_string(points, triangles)
    to_binary_string_duration = time.perf_counter() - start

    start = time.perf_counter()
    pts2, tris2 = to_lists(data)
    to_lists_duration = time.perf_counter() - start
    print(f"serialize {n} points in {to_binary_string_duration:.3f}s, deserialize in {to_lists_duration:.3f}s")
    assert pts2 == points
    assert tris2 == triangles
    assert to_binary_string_duration < 2
    assert to_lists_duration < 2