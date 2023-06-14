# Slide Generator

Slide Generator is a web application that generates slide content based on user input. It utilizes the OpenAI GPT-3.5 language model to generate educational slide content for various grades.

## Features

- Generate slide content for a given title, grade, and number of slides.
- Utilizes the OpenAI GPT-3.5 language model for generating educational content.
- Supports grades from 1st to 9th grade.
- Options to generate 3, 5, 10, or 15 slides.
- Generates output in PowerPoint (.pptx) format.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Flask 2.0.1
- requests 2.26.0
- python-pptx
- OpenAI's API KEY

### Installation

1. Clone the repository:

```shell
git clone https://github.com/your-username/slide-generator.git
```
2. Install the required dependencies:
```
pip install -r requirements.txt

```
### Usage
1. Run the Flask app:
    ```
    python app.py
    ```
2. Access the application in your web browser at ```192.168.56.1:9000```
3. Fill in the required details: Title, Grade, and Number of Slides.
4. Click on *Generate Slides* to generate the slide content.
5. The generated slide content will be displayed below the form.
6. The generated slides will be saved as **output.pptx** in the *templates* folder.

## Contribution
Contributions are welcome! If you find any issues or want to contribute enhancements, please open a new issue or submit a pull request.

## License
This project is licensed under the MIT License.
Feel free to customize it further based on your project's specific details and requirements.

