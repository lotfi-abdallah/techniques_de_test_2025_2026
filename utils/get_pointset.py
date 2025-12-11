"""Fetch PointSet data from PointSetManager API."""
import requests


def get_pointset(pointset_id: str) -> bytes:
    """Fetch a PointSet from the PointSetManager API."""
    url = f"http://127.0.0.1:5000/pointset/{pointset_id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.content