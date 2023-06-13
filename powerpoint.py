import json
import os
import requests
from flask import Flask, render_template, request, jsonify
from pptx import Presentation

API_KEY = "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"

app = Flask(__name__)

@app.route("/")
def index():
    title = request.args.get("title")
    grade = request.args.get("grade")
    num_slides = request.args.get("num_slides")

    if title is None or grade is None or num_slides is None:
        return render_template("index.html")

    prompt = f'''
    Prepare {num_slides} slides about {title} for {grade} grade students. You must be following the structure of the example given below, where each heading must contain 4 bullet points
    Example: Title: "Unbalanced trees"
    1. If a BST is not balanced, its time complexity can degrade to O(n)
    2. Inefficient operations: BSTs do not provide efficient support for some operations such as finding the kth smallest 
    3. Not efficient on duplicates and skewness
    4. Space complexity: BSTs require a lot of memory allocation
    '''
    print()
    print("------------")
    print(prompt)
    print()
    print("------------")
    # Get the response from ChatGPT
    response = requests.post(
        "https://api.openai.com/v1/engines/davinci/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        data=json.dumps({
            "prompt": prompt,
            "temperature": 0.7,
            "max_tokens": 5000,
            "no_repeat_ngrams": 2,
            "include_prompt": False,
        }),
    )

    # Parse the response
    response_json = response.json()
    print(response_json)
    slides = response_json["choices"][0]["text"].split("\n")

    # Render the template with the slides
    render_template("index.html", slides=slides)

    # Create a new PowerPoint presentation
    presentation = Presentation()

    # Iterate through the slides data and create slides
    for slide_text in slides:
        slide_layout = presentation.slide_layouts[1]  # Choose the slide layout (Title and Content)
        slide = presentation.slides.add_slide(slide_layout)

        title_shape = slide.shapes.title
        title_shape.text = title

        content_slide = slide.placeholders[1]
        points = slide_text.split('\n')
        for point in points:
            content_slide.text_frame.add_paragraph().text = point

    # Save the presentation
    presentation.save("output.pptx")

    print('Slides created successfully!')

if __name__ == "__main__":
    app.run(debug=True)
