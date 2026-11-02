from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    user_input = request.form.get('user_input')
    # Do something with the input – here we reverse it
    result = user_input[::-1]
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)