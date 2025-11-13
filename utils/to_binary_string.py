import struct

def to_binary_string(points, triangles):
    """
    Convert a list of vertices and triangles to the required binary format.

    points: list of (x, y)
    triangles: list of (i, j, k)
    """
    # Start with vertex count
    binary_data = struct.pack('<I', len(points))  # < = little-endian, I = unsigned int (4 bytes)
    
    # Add all vertices (float32 x, float32 y)
    for x, y in points:
        binary_data += struct.pack('<ff', x, y)
    
    # Add triangle count
    binary_data += struct.pack('<I', len(triangles))
    
    # Add all triangles (3 × uint32 indices)
    for a, b, c in triangles:
        binary_data += struct.pack('<III', a, b, c)
    
    return binary_data

def to_lists(binary_data):
    """
    Convert binary data back to lists of vertices and triangles.

    Returns (points, triangles)
    points: list of (x, y)
    triangles: list of (i, j, k)
    """
    offset = 0
    
    # Read vertex count
    vertex_count = struct.unpack_from('<I', binary_data, offset)[0]
    offset += 4
    
    points = []
    for _ in range(vertex_count):
        x, y = struct.unpack_from('<ff', binary_data, offset)
        points.append((x, y))
        offset += 8  # 2 floats of 4 bytes each
    
    # Read triangle count
    triangle_count = struct.unpack_from('<I', binary_data, offset)[0]
    offset += 4
    
    triangles = []
    for _ in range(triangle_count):
        a, b, c = struct.unpack_from('<III', binary_data, offset)
        triangles.append((a, b, c))
        offset += 12  # 3 uint32 of 4 bytes each
    
    return points, triangles