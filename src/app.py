from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/generate")
def generate():
    keyword = request.args.get("keyword", "default")

    return jsonify({"message": f"You sent: {keyword}"})


if __name__ == "__main__":
    app.run(debug=True)
