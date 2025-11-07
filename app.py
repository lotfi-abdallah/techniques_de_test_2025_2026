from flask import Flask

app = Flask(__name__)

@app.route("/triangulation/<pointSetId>", methods=["GET"])
def get_triangulation(pointSetId):
    # return dummy json with 'vertices and 'triangles' keys
    return {
        "vertices": [[0, 0], [1, 0], [0, 1]],
        "triangles": [[0, 1, 2]]
    } 

if __name__ == "__main__":
    app.run(debug=True)