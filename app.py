from flask import Flask, jsonify, request

app = Flask(__name__)


def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def get_user_status(age):
    return "Adult" if age >= 18 else "Minor"


@app.route("/")
def home():
    return jsonify({"message": "Application is running"})


@app.route("/add")
def addition():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    return jsonify({"result": add(a, b)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

