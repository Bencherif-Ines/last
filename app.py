from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/add/<int:numberA>/<int:numberB>')
def add(numberA, numberB):
    result = numberA + numberB
    return jsonify(status=200, result=result)

@app.route('/minus/<int:numberA>/<int:numberB>')
def minus(numberA, numberB):
    result = numberA - numberB
    return jsonify(status=200, result=result)

@app.route('/multiply/<int:numberA>/<int:numberB>')
def multiply(numberA, numberB):
    result = numberA * numberB
    return jsonify(status=200, result=result)

@app.route('/divide/<int:numberA>/<int:numberB>')
def divide(numberA, numberB):
    if numberB == 0:
        return jsonify(status=400, result="Cannot divide by zero"), 400
    result = numberA / numberB
    return jsonify(status=200, result=result)

if __name__ == '__main__':
    app.run(debug=True)
