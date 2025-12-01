import struct
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))
from utils.to_binary_string import to_binary_string, to_lists


def test_to_binary_string_basic():
    points = [(0.0, 0.0), (1.0, 0.0), (0.0, 1.0)]
    triangles = [(0, 1, 2)]

    expected = struct.pack('<I', len(points))
    for x, y in points:
        expected += struct.pack('<ff', x, y)
    expected += struct.pack('<I', len(triangles))
    for a, b, c in triangles:
        expected += struct.pack('<III', a, b, c)

    result = to_binary_string(points, triangles)
    assert isinstance(result, (bytes, bytearray))
    assert result == expected

def test_to_binary_string_empty():
    points = []
    triangles = []

    expected = struct.pack('<I', 0) + struct.pack('<I', 0)
    result = to_binary_string(points, triangles)
    assert result == expected

def test_to_binary_string_non_integer_coords_and_multiple_triangles():
    points = [(1.5, -2.0), (3.25, 4.75)]
    triangles = [(0, 1, 0), (1, 0, 1)]

    expected = struct.pack('<I', len(points))
    for x, y in points:
        expected += struct.pack('<ff', x, y)
    expected += struct.pack('<I', len(triangles))
    for a, b, c in triangles:
        expected += struct.pack('<III', a, b, c)

    result = to_binary_string(points, triangles)
    assert result == expected

def test_one_triangle_roundtrip_from_binary_to_list():
    points = [(0.0, 0.0), (1.0, 0.0), (0.0, 1.0)]
    triangles = [(0, 1, 2)]

    binary_data = to_binary_string(points, triangles)
    recovered_points, recovered_triangles = to_lists(binary_data)

    assert recovered_points == points
    assert recovered_triangles == triangles

def test_multiple_triangles_roundtrip_from_binary_to_list():
    points = [(float(i), float((i * 7) % 10)) for i in range(50)]
    triangles = [(i, i + 1, i + 2) for i in range(0, 47)]
    binary = to_binary_string(points, triangles)
    pts2, tris2 = to_lists(binary)
    assert pts2 == points
    assert tris2 == triangles