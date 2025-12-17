Module tp1.app
==============
Flask application for the Triangulator microservice.

Provides HTTP API endpoints for triangulating point sets retrieved from
the PointSetManager service.

Functions
---------

`get_triangulation(pointSetId)`
:   Retrieve and triangulate a point set.
    
    Args:
        pointSetId: UUID of the point set to triangulate.
    
    Returns:
        Binary response with triangulated data (200), or JSON error
        (404 if not found, 400 if malformed, 500 if triangulation fails,
        503 if PointSetManager unavailable).