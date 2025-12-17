Module tp1.utils.to_binary_string
=================================
Utility functions.

for converting between point/triangle lists and binary string format.

Functions
---------

`to_binary_string(points, triangles)`
:   Convert a list of vertices and triangles to the required binary format.
    
    points: list of (x, y)
    triangles: list of (i, j, k)

`to_lists(binary_data)`
:   Convert binary data back to lists of vertices and triangles.
    
    Returns (points, triangles)
    points: list of (x, y)
    triangles: list of (i, j, k)
    
    Raises struct.error if the binary data is malformed.