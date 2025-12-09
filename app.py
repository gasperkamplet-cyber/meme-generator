from flask import Flask, render_template, request, redirect, url_for
from PIL import Image, ImageDraw, ImageFont
import os
import uuid


app = Flask(__name__)
UPLOAD_FOLDER = "static/memes"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        image_file = request.files["image"]
        top_text = request.form.get("top_text", "")
        bottom_text = request.form.get("bottom_text", "")

        if image_file:
            img = Image.open(image_file)
            draw = ImageDraw.Draw(img)

            font_size = int(img.height / 10)
            try:
                font = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", font_size)
            except:
                font = ImageFont.load_default()

            draw.text(
                (img.width / 2, 0),
                top_text,
                font=font,
                fill="white",
                anchor="ma",
                stroke_width=2,
                stroke_fill="black"
            )

            y_position = img.height - int(img.height * 0.05)
            draw.text(
                (img.width / 2, y_position),
                bottom_text,
                font=font,
                fill="white",
                anchor="ms",
                stroke_width=2,
                stroke_fill="black"
            )

            meme_filename = f"{uuid.uuid4().hex}.png"
            meme_path = os.path.join(UPLOAD_FOLDER, meme_filename)
            img.save(meme_path)

            return redirect(url_for("index", meme=meme_filename))

    meme_file = request.args.get("meme")
    return render_template("index.html", meme=meme_file)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
