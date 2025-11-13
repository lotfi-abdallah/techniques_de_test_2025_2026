import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from configure_tests import client,app

# Error:
#       type: object
#       properties:
#         code:
#           type: string
#           description: An internal error code.
#           example: 'TRIANGULATION_FAILED'
#         message:
#           type: string
#           description: A human-readable error message.
#           example: 'Triangulation could not be computed for the given point set.'
#       required:
#         - code
#         - message

def test_get_triangulation_nominal(client):
    """Test the /triangulation endpoint with a valid PointSet ID."""
    response = client.get("/triangulation/123e4567-e89b-12d3-a456-426614174000")
    assert response.status_code == 200
    
    assert response.content_type == 'application/octet-stream'
    data = response.data
    assert isinstance(data, bytes)

def test_get_triangulation_invalid_id(client):
    """Test the /triangulation endpoint with an invalid PointSet ID."""
    #  '404':
    #       description: The specified PointSetID was not found (as reported by the PointSetManager).
    #       content:
    #         application/json:
    #           schema:
    #             $ref: '#/components/schemas/Error'
    response = client.get("/triangulation/invalid-id")
    assert response.status_code == 404

    assert response.content_type == 'application/json'
    data = response.get_json()
    assert 'error' in data
    assert data['error']['code'] == 'POINTSET_NOT_FOUND'
    assert data['error']['message'] == 'The specified PointSetID was not found.'
