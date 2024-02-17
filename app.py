from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        input_text = request.form['input_text']
        # Do something with the input_text, for example, print it
        print("Input text:", input_text)
        return "Input received: " + input_text
    else:
        return "Error: Only POST requests are allowed."

if __name__ == '__main__':
    app.run(debug=True)
