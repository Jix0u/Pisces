from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from gtts import gTTS
import cohere
import json

import moviepy.editor as mpe

app = Flask(__name__)
app.secret_key = "super secret key"
api_key = "PGUxIRQ8zWBUt2nTfQbyIDxL1eg0up6DluMwGyfd"
co = cohere.Client(api_key)
# Dummy user database for demonstration purposes
users = {"user1": "password1", "user2": "password2"}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/prompt-page")
def index1():
    return render_template("prompt.html")


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
            return redirect(url_for("index1"))
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
    generated_advertisement = co.chat(
        message=f'Using this information for my product, "{prediction.text}", I want you to create a unique and creative advertisement that targets the stated target audience and fits the mentionned social media platforms. Can you also put it in the format of a JSON object, with fields like "Instagram" and "TikTok" for its respective script, also only give me the JSON object, dont write anything else. In the json object, only give me the different social media platforms, with a caption and script, only use lowercase characters.'
    )
    generated_advertisement.text = generated_advertisement.text[8:-4]
    language = "en"
    jsonObj = json.loads(generated_advertisement.text)

    for platform in list(jsonObj):
        obj = gTTS(jsonObj[platform]["script"], lang=language, slow=False)
        obj.save(f"{platform}.mp3")

    platform_tmp = list(jsonObj)[0]
    return platform_tmp


def combine_audio(audname, music_name):
    audio_clip = mpe.AudioFileClip(audname)
    audio_clip_midi = mpe.AudioFileClip(music_name).volumex(0.1)
    audio_duration = audio_clip.duration
    audio_clip_midi = audio_clip_midi.set_duration(audio_duration)
    final_audio_clip = mpe.CompositeAudioClip([audio_clip, audio_clip_midi])
    return final_audio_clip


def combine_files(vidname, audname, midi_file, outname, fps=60):
    # Load video and audio clips
    video_clip = mpe.VideoFileClip(vidname)
    audio_clip = combine_audio(audname, midi_file)

    audio_duration = audio_clip.duration
    num_loops = int(audio_duration / video_clip.duration) + 1
    final_video_clip = mpe.concatenate_videoclips([video_clip] * num_loops)
    final_video_clip = final_video_clip.set_audio(audio_clip)
    outname = "static/" + outname
    final_video_clip.write_videofile(outname, fps=fps)


@app.route("/upload", methods=["POST"])
def upload_video():
    if "video" in request.files:
        video_file = request.files["video"]
        video_file.save("earbuds.mp4")  # Save the uploaded video file
        return "Video uploaded successfully!", 200
    else:
        return "No video file in the request!", 400


@app.route("/get_prediction", methods=["POST"])
def get_prediction():
    product_name = request.form["product_name"]
    product_description = request.form["product_description"]

    # Generate a prompt using product name and description
    prompt = f"Product: {product_name}\nDescription: {product_description}\n"

    # Generate prediction from Cohere
    prediction = co.chat(
        message="Develop a Comprehensive Marketing Plan for the product"
        + product_name
        + "."
        + "The product description is:"
        + product_description
        + "Say who is the possible audience, best social media platform to generate ads, what method of ads are the best based on the product.",
        model="command",
    )

    pred = generate_voiceover(prediction)

    file_name = "video/" + product_name + ".mp4"
    platform_audio = pred + ".mp3"
    combine_files(file_name, platform_audio, "drum.mp3", "output.mp4")

    return jsonify({"response": prediction.text, "video_path": "../static/output.mp4"})


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
