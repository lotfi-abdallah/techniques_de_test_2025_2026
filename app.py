from flask import Flask

app = Flask(__name__)

@app.route("/triangulation/<pointSetId>", methods=["GET"])
def get_triangulation(pointSetId):
    # return dummy bytes for testing purposes
    dummy_data = b'\x00'  # Example of binary data
    return dummy_data, 200, {'Content-Type': 'application/octet-stream'}

if __name__ == "__main__":
    app.run(debug=True)