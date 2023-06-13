import json
import os
import requests
from flask import Flask, render_template, request, jsonify

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
            "Authorization": "Bearer YOUR_API_KEY",
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
    if 'choices' in response_json and len(response_json['choices']) > 0:
        slides = response_json['choices'][0]['text'].split("\n")
    else:
        # Handle error when 'choices' key is not present
        slides = []

    # Render the template with the slides
    return render_template("index.html", slides=slides)

if __name__ == "__main__":
    app.run(debug=True)
