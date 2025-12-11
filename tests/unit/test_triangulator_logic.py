"""Unit tests for triangulation algorithm logic."""
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

import pytest

import triangulator
from tests.helpers.pointsets import (
    colinear_line,
    duplicate_points,
    polygon_convex,
    square_ccw,
    triangle,
)


@pytest.mark.unit
def test_empty_points_returns_no_triangles():
    """Test that empty pointset returns no triangles."""
    assert triangulator.triangulate([]) == []

@pytest.mark.unit
def test_single_point_returns_no_triangles():
    """Test that single point returns no triangles."""
    assert triangulator.triangulate([(0.0, 0.0)]) == []

@pytest.mark.unit
def test_two_points_returns_no_triangles():
    """Test that two points return no triangles."""
    assert triangulator.triangulate([(0.0, 0.0), (1.0, 0.0)]) == []

@pytest.mark.unit
def test_colinear_points_returns_empty():
    """Test that colinear points return no triangles."""
    pts = colinear_line()
    tris = triangulator.triangulate(pts)
    assert tris == []

@pytest.mark.unit
def test_three_points_returns_one_triangle():
    """Test that three points return one triangle."""
    pts = triangle()
    tris = triangulator.triangulate(pts)
    assert isinstance(tris, list)
    assert len(tris) == 1
    a, b, c = tris[0]
    assert set((a, b, c)) == {0, 1, 2}

@pytest.mark.unit
def test_convex_square_returns_two_triangles():
    """Test that a convex square returns two triangles."""
    # square in counter-clockwise order
    pts = square_ccw()
    tris = triangulator.triangulate(pts)
    assert isinstance(tris, list)
    assert len(tris) == 2
    # triangles indices should reference vertices 0..3
    all_idx = set(i for t in tris for i in t)
    assert all_idx <= {0, 1, 2, 3}

@pytest.mark.unit
def test_convex_polygon_returns_n_minus_2_triangles():
    """Test that a convex polygon returns (n-2) triangles."""
    pts = polygon_convex(n=5)
    tris = triangulator.triangulate(pts)
    assert isinstance(tris, list)
    assert len(tris) == 3  # for n=5, should return 3 triangles
    all_idx = set(i for t in tris for i in t)
    assert all_idx <= {0, 1, 2, 3, 4}

@pytest.mark.unit
def test_duplicate_points_handled():
    """Test that duplicate points are handled correctly."""
    pts = duplicate_points()
    tris = triangulator.triangulate(pts)
    # After removing duplicates we still have a triangle
    assert isinstance(tris, list)
    assert len(tris) == 1