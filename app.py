from flask import Flask, render_template, request, redirect
from detect_bubbles import detect_bubbles
from process_bubble import process_bubble
from translator.translator import MangaTranslator
from add_text import add_text
from manga_ocr import MangaOcr
from PIL import Image
import numpy as np
import cv2
import base64

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"

MODEL_PATH = "model/model.pt"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/translate", methods=["POST"])
def upload_file():

    if "Opus-mt model" == request.form["selected_translator"]:
        selected_translator = "hf"
    else:
        selected_translator = request.form["selected_translator"].lower()

    selected_font = request.form["selected_font"].lower()

    if "file" in request.files:
        file = request.files["file"]
        name = file.filename.split(".")[0]

        if file.filename != '':

            image = cv2.imread(file)

            results = detect_bubbles(MODEL_PATH, image)

            manga_translator = MangaTranslator()
            mocr = MangaOcr()

            for result in results:
                x1, y1, x2, y2, score, class_id = result

                detected_image = image[int(y1):int(y2), int(x1):int(x2)]

                im = Image.fromarray(np.uint8(detected_image * 255))
                text = mocr(im)

                detected_image, cont = process_bubble(detected_image)
                text_translated = manga_translator.translate(text, method=selected_translator)

                add_text(detected_image, text_translated, f"fonts/{selected_font}i.ttf", cont)

            _, buffer = cv2.imencode('.png', image)
            image = buffer.tobytes()
            encoded_image = base64.b64encode(image).decode('utf-8')

            return render_template("translate.html", name=name, uploaded_image=encoded_image)
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
