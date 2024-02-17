from flask import Flask, render_template, request, jsonify
import api_key from apikey
import cohere

app = Flask(__name__)
co = cohere.Client(api_key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_prediction', methods=['POST'])
def get_prediction():
    product_name = request.form['product_name']
    product_description = request.form['product_description']
    
    # Generate a prompt using product name and description
    prompt = f'Product: {product_name}\nDescription: {product_description}\n'

    # Generate prediction from Cohere
    prediction = co.chat(message='Develop a Comprehensive Marketing Plan for the product' + product_name + '.' + 'The product description is:' + product_description  + 'Say who is the possible audience, best social media platform to generate ads, what method of ads are the best based on the product.', model='command')

    return jsonify({'response': prediction.text})

if __name__ == '__main__':
    app.run(debug=True)
