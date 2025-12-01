import sys
from pathlib import Path
from unittest.mock import patch
import pytest

sys.path.append(str(Path(__file__).parent.parent))

from configure_tests import client,app


from utils.to_binary_string import to_binary_string
from tests.helpers.pointsets import triangle as make_points


def test_triangulation_happy_path(client):
    pts = make_points()
    fake_pointset = to_binary_string(pts, [])

    # We expect the future implementation to call `get_pointset(pointSetId)`
    with patch('app.get_pointset', return_value=fake_pointset):
        response = client.get('/triangulation/11111111-1111-1111-1111-111111111111')

    assert response.status_code == 200
    assert response.content_type == 'application/octet-stream'
    assert isinstance(response.data, (bytes, bytearray))


def test_pointset_not_found_returns_404(client):
    # we expect "not-found" to be an invalid ID for this test
    with patch('app.get_pointset', side_effect=FileNotFoundError):
        response = client.get('/triangulation/not-found')

    assert response.status_code == 404
    assert response.content_type == 'application/json'
    data = response.get_json()
    assert 'error' in data
    assert data['error']['code'] == 'POINTSET_NOT_FOUND'


def test_malformed_pointset_returns_400(client):
    # return bytes that cannot be parsed
    with patch('app.get_pointset', return_value=b'$$not-a-valid-pointset$$'):
        response = client.get('/triangulation/bad-bytes')

    assert response.status_code == 400
    assert response.content_type == 'application/json'
    data = response.get_json()
    assert data['error']['code'] == 'INVALID_POINTSET'


def test_triangulation_failure_returns_500(client):
    pts = make_points()
    fake_pointset = to_binary_string(pts, [])

    # Simulate triangulator raising a domain-specific error
    class DummyError(Exception):
        pass

    # Patch get_pointset to return a valid blob, and triangulator.triangulate to raise
    with patch('app.get_pointset', return_value=fake_pointset):
        with patch('triangulator.triangulate', side_effect=Exception('fail')):
            response = client.get('/triangulation/123')

    assert response.status_code == 500
    assert response.content_type == 'application/json'
    data = response.get_json()
    assert data['error']['code'] == 'TRIANGULATION_FAILED'
