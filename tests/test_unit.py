import sys
from pathlib import Path
import struct
sys.path.append(str(Path(__file__).parent.parent))
from utils.to_binary_string import to_binary_string

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

def test_from_binary_string_to_list():
    from utils.to_binary_string import to_lists

    points = [(0.0, 0.0), (1.0, 0.0), (0.0, 1.0)]
    triangles = [(0, 1, 2)]

    binary_data = to_binary_string(points, triangles)
    recovered_points, recovered_triangles = to_lists(binary_data)

    assert recovered_points == points
    assert recovered_triangles == triangles