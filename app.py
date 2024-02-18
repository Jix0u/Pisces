from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from gtts import gTTS
import cohere
import json


app = Flask(__name__)
app.secret_key = (
    ""  # Change this to your secret key
)
co = cohere.Client("s")

# Dummy user database for demonstration purposes
users = {"user1": "password1", "user2": "password2"}




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prompt-page')
def index1():
    return render_template('prompt.html')


# Route for login page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Check if the username and password match
        if username in users and users[username] == password:
            # If the user exists and the password is correct, set the session variable and redirect to the index page
            session["username"] = username
            return redirect(url_for("index"))
        else:
            # If the username or password is incorrect, render the login page with an error message
            return render_template("login.html", error="Invalid username or password.")

    # If the request method is GET, render the login page
    return render_template("login.html")


# Route for signup page
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Add the new user to the database
        users[username] = password
        return redirect(url_for("login"))

    return render_template("signup.html")


def generate_voiceover(prediction):
    generated_advertisement = co.chat(message=f'Using this information for my product, "{prediction.text}", I want you to create a unique and creative advertisement that targets the stated target audience and fits the mentionned social media platforms. Can you also put it in the format of a JSON object, with fields like "Instagram" and "TikTok" for its respective script, also only give me the JSON object, dont write anything else. In the json object, only give me the different social media platforms, with a caption and script, only use lowercase characters.')
    generated_advertisement.text = generated_advertisement.text[8:-4]
    language = 'en'
    jsonObj = json.loads(generated_advertisement.text)
    for platform in list(jsonObj):
        obj = gTTS(jsonObj[platform]["script"], lang=language, slow=False)
        obj.save(f"{platform}.mp3")
    return jsonify({"advertisement": generated_advertisement.text})


@app.route('/get_prediction', methods=['POST'])
def get_prediction():
    product_name = request.form['product_name']
    product_description = request.form['product_description']
    
    # Generate a prompt using product name and description
    prompt = f'Product: {product_name}\nDescription: {product_description}\n'

    # Generate prediction from Cohere
    prediction = co.chat(message='Develop a Comprehensive Marketing Plan for the product' + product_name + '.' + 'The product description is:' + product_description  + 'Say who is the possible audience, best social media platform to generate ads, what method of ads are the best based on the product.', model='command')

    generate_voiceover(prediction)

    return jsonify({'response': prediction.text})

@app.route("/complete")
def complete():
    return render_template("complete.html")


@app.route("/payment")
def payment():
    return render_template("payment.html")


@app.route("/in_depth")
def in_depth():
    return render_template("in_depth.html")


if __name__ == "__main__":
    app.run(debug=True)
