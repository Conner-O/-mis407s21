from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("calc-form.html")


@app.route('/compute', methods=['POST'])
def compute(result=sum):
    if request.method == 'POST':
        num1 = request.form['number1']
        num2 = request.form['number2']
        operation = request.form['operator']

        if operation == '+':
            result = float(num1) + float(num2)
            return render_template('calc-result.html', result=result)

        elif operation == '-':
            result = float(num1) - float(num2)
            return render_template('calc-result.html', result=result)

        elif operation == '*':
            result = float(num1) * float(num2)
            return render_template('calc-result.html', result=result)

        elif operation == '/':
            result = float(num1) / float(num2)
            return render_template('calc-result.html', result=result)
        else:
            return render_template('calc-result.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)