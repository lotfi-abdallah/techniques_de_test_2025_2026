import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from configure_tests import client,app

def test_get_triangulation_nominal(client):
    """Test the /triangulation endpoint with a valid PointSet ID."""
    response = client.get("/triangulation/123e4567-e89b-12d3-a456-426614174000")
    assert response.status_code == 200
    
    assert response.content_type == 'application/octet-stream'
    data = response.data
    assert isinstance(data, bytes)



