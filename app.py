from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2
        else:
            result = 'Invalid operation'

        return render_template('calculator.html', num1=num1, num2=num2, operation=operation, result=result)
    except Exception as e:
        return render_template('calculator.html', result=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Change to your desired port
