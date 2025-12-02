import struct
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

import pytest

from utils.to_binary_string import to_binary_string, to_lists

@pytest.mark.unit
def test_to_lists_truncated_header_raises():
    with pytest.raises((struct.error, Exception)):
        to_lists(b'')

@pytest.mark.unit
def test_to_lists_incomplete_point_data_raises():
    # header says 2 points, but no bytes follow
    binary = struct.pack('<I', 2)
    with pytest.raises((struct.error, Exception)):
        to_lists(binary)

@pytest.mark.unit
def test_to_lists_incomplete_triangle_data_raises():
    # one valid point, triangle header says 1 triangle but triangle bytes missing
    points = [(0.0, 0.0)]
    # craft binary with 1 point
    binary = to_binary_string(points, [])
    # append triangle-count but not enough triangle bytes
    binary += struct.pack('<I', 1)
    with pytest.raises((struct.error, Exception)):
        to_lists(binary)
