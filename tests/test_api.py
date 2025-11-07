import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from configure_tests import client,app

def test_get_triangulation_nominal(client):
    """Test the /triangulation endpoint with a valid PointSet ID."""
    response = client.get("/triangulation/123e4567-e89b-12d3-a456-426614174000")
    assert response.status_code == 200
    data = response.get_json()

    assert 'vertices' in data, "Missing 'vertices' key in response"
    assert 'triangles' in data, "Missing 'triangles' key in response"

    assert len(data['vertices']) > 0, "Vertices list is empty"
    assert len(data['triangles']) > 0, "Triangles list is empty"


