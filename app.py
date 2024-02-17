from flask import Flask, render_template, request, jsonify
import api_key from apikey
from gtts import gTTS
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

@app.route('/generate_voiceover', methods=['POST'])
def generate_voiceover():
    data = request.json
    product_name = data['product_name']
    product_description = data['product_description']
    target_audience = data['target_audience']
    social_media_platforms = data['social_media_platforms']
    generated_advertisement = co.chat(message=f'Create an advertisement for a product called "{product_name}". The product description is: "{product_description}". I want you to create a unique and creative advertisement that targets {target_audience} and fits the following social media platforms, {social_media_platforms}. Can you also put it in the format of a JSON object, with fields like "Instagram" and "TikTok" for its respective script, also only give me the JSON object, dont write anything else')
    print(generated_advertisement.text)
    language = 'en'
    obj = gTTS(text=generated_advertisement.text, lang=language, slow=False)
    obj.save("audio.mp3")
    return jsonify({"advertisement": generated_advertisement.text})

if __name__ == '__main__':
    app.run(debug=True)
