# Import necessary modules
from flask import Flask, render_template, request

# Create a Flask app
app = Flask(__name__)

# Define routes and views
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print(param) 
    return param   

@app.route('/count/<int:param>')
def count(param):
    numbers = '\n'.join(str(num) for num in range(param))
    return numbers

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid operation'

    if result is not None:
        return str(result)
    else:
        return 'Cannot divide by zero'

# Run the app
if __name__ == '__main__':
    app.run(port=5555)
