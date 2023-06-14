import json
import os
import requests
from flask import Flask, render_template, request, jsonify
import collections 
import collections.abc
from pptx import Presentation

API_KEY = "KEY"

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
    #print(response_json)
    slides = response_json["choices"][0]["text"].split("\n")
    # print(slides)
    # this variable is for testing slides variable indexing
    slide_list = slides
    # print(slide_list)
    slide_list_filtered = [slide for slide in slide_list if slide != '']

    presentation = Presentation()
    for i in range(0, len(slide_list_filtered), 2):
        slide_number = slide_list_filtered[i]
        slide_description = slide_list_filtered[i + 1] if i + 1 < len(slide_list_filtered) else ""
        slide = presentation.slides.add_slide(presentation.slide_layouts[1])
        title = slide.shapes.title
        title.text = slide_number
        content = slide.placeholders[1]
        content.text = slide_description

    presentation.save(r"C:\Users\dell\Desktop\Slide Generator\SlidesGenerator\templates\output.pptx")

    return render_template("index.html", slides=slides)

if __name__ == "__main__":
    app.run(host="192.168.56.1", port=9000, debug=True)