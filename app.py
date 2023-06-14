import json
import os
import requests
from flask import Flask, render_template, request, jsonify
from pptx import Presentation

API_KEY = ""

app = Flask(__name__)
slides = []

@app.route("/")
def index():
    title = request.args.get("title")
    grade = request.args.get("grade")
    num_slides = request.args.get("num_slides")
    if title is None or grade is None or num_slides is None:
        return render_template("index.html")
    prompt = f"""
    Give content for {num_slides} slides on the topic '{title}' for Grade {grade} Students 
    """
    print()
    print("------------")
    print(prompt)  # Debugger Check
    print()
    print("------------")
    response = requests.post(
        "https://api.openai.com/v1/engines/text-davinci-003/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "prompt": f"Give content for {num_slides} slides on the topic '{title}' for Grade {grade} Students",
            "temperature": 0,
            "max_tokens": 2000,
        }
    )


    response_json = response.json()
    print(response_json)
    slides = response_json["choices"][0]["text"].split("\n")
    return render_template("index.html", slides=slides)

@app.route("/generate", methods=["GET"])
def generate_slides():
    title = request.args.get("title")
    num_slides = request.args.get("num_slides")
    presentation = Presentation()
    for slide_text in slides:
        slide_layout = presentation.slide_layouts[1]  # Choose the slide layout (Title and Content)
        slide = presentation.slides.add_slide(slide_layout)
        title_shape = slide.shapes.title
        title_shape.text = title

        content_slide = slide.placeholders[1]
        points = slide_text.split("\n")
        for point in points:
            content_slide.text_frame.add_paragraph().text = point
    print("Before Save is called")
    presentation.save(r"C:\Users\dell\Desktop\Slide Generator\SlidesGenerator\templates\output.pptx")
    print("Slides created successfully!")
    return "Slides created successfully!"

if __name__ == "__main__":
    app.run(host="192.168.56.1", port=9000, debug=True)