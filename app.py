from flask import Flask, jsonify

import triangulator
from utils.get_pointset import get_pointset
from utils.to_binary_string import to_binary_string, to_lists

app = Flask(__name__)

@app.route("/triangulation/<pointSetId>", methods=["GET"])
def get_triangulation(pointSetId):
    try:
        data = get_pointset(pointSetId)
    except FileNotFoundError:
        return jsonify({
            'error': {
                'code': 'POINTSET_NOT_FOUND',
                'message': 'The specified PointSetID was not found.'
            }
        }), 404
    except ConnectionError:
        return jsonify({
            'error': {
                'code': 'POINTSET_SERVICE_UNAVAILABLE',
                'message': 'Could not connect to the PointSet service.'
            }
        }), 503

    try:
        # `to_lists` expects a binary containing points and (optional) triangles.
        points, _ = to_lists(data)
    except Exception:
        return jsonify({
            'error': {
                'code': 'INVALID_POINTSET',
                'message': 'PointSet bytes are malformed.'
            }
        }), 400

    try:
        triangles = triangulator.triangulate(points)
    except Exception:
        return jsonify({
            'error': {
                'code': 
                'TRIANGULATION_FAILED',
                'message':
                'Triangulation could not be computed for the given point set.'
            }
        }), 500

    out = to_binary_string(points, triangles)
    return out, 200, {'Content-Type': 'application/octet-stream'}

if __name__ == "__main__":
    app.run(debug=True)