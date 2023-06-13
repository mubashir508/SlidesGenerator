from pptx import Presentation

# Define your slide data
slide_data = {
    "slides": [
        {
            "title": "Introduction to Our Solar System",
            "points": [
                "What is the Solar System?",
                "Components of the Solar System",
                "Size and Scale of the Solar System",
                "Importance of studying the Solar System"
            ]
        }
    ]
}

# Create a new PowerPoint presentation
presentation = Presentation()

# Iterate through the slides data and create slides
for slide in slide_data['slides']:
    slide_layout = presentation.slide_layouts[1]  # Choose the slide layout (Title and Content)
    slide = presentation.slides.add_slide(slide_layout)

    title = slide.shapes.title
    title.text = slide['title']

    content_slide = slide.placeholders[1]
    for point in slide['points']:
        content_slide.text_frame.add_paragraph().text = point

# Save the presentation
presentation.save("output.pptx")

print('Slides created successfully!')
