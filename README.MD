# Website Content Generator

The Website Content Generator is a Flask web application that allows users to generate a simple, responsive HTML and CSS code pair based on a text brief. The application uses OpenAI's GPT-3 model to generate the content. Users input a brief, and the application outputs a live preview of the generated website, viewable on mobile, desktop, and large desktop screen sizes.

## Table of Contents

- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Files and Functionalities](#files-and-functionalities)
- [Usage Examples](#usage-examples)
- [Contributing and Maintaining](#contributing-and-maintaining)

## Getting Started

To get started, clone the repository and set up a Python virtual environment:

### Prerequisites

1. Python 3.x
2. Flask
3. OpenAI

### Installation

```bash
git clone https://github.com/your-repository/WebsiteContentGenerator.git
cd WebsiteContentGenerator
python -m venv venv
source venv/bin/activate # For Linux and macOS
venv\Scripts\activate # For Windows
pip install -r requirements.txt
```

To run the application:

```bash
python app.py
```

Visit `http://127.0.0.1:5000/` in your browser to access the Website Generator page.

## Project Structure

The application's structure consists of the following components:

```
.
├── app.py
├── generator.py
├── file_handler.py
├── main.py
├── requirements.txt
├── README.md
├── templates
│   └── index.html
└── static
    ├── css
    │   └── style.css
    ├── js
    │   └── app.js
    └── generated
        └── preview
            ├── index.html
            └── styles.css
```

## Technologies Used

- [Flask](https://flask.palletsprojects.com/): A micro web framework for Python used to build the web application.
- [Python](https://www.python.org/): The main programming language used for the project.
- [OpenAI GPT-3](https://beta.openai.com/): An artificial intelligence language model used to generate HTML and CSS content based on user input.
- [HTML, CSS, and JavaScript](https://www.w3.org/standards/webdesign/htmlcss.html): Frontend languages used for designing the website template and handling user interactions.

## Files and Functionalities

### `app.py`

This file contains the main Flask application setup and routing. The application defines a single route `/` with methods `GET` and `POST`.

When generating a website, the app receives a brief (`POST`), generates the HTML and CSS files for the website, and then stores the files in the `'static/generated/preview/'` folder. The preview URL is passed to the `index.html` template to display the generated website within an iframe in both mobile and desktop views.

### `generator.py`

This file contains the `WebsiteGenerator` class that generates HTML and CSS content based on the user's input. The class uses OpenAI's GPT-3 model to generate the content. The result is returned as a tuple containing the HTML and CSS code as strings.

### `file_handler.py`

This file contains the `FileHandler` class that handles file creation, deletion, and compression for preview and download purposes. The class is responsible for saving and managing the generated files for the website.

### `main.py`

This file is responsible for the main logic of generating the website files. The `generate_website_files` function takes a brief as input and calls the `generate_html_css` method from the `WebsiteGenerator` class to produce the HTML and CSS code.

Then, the `save_to_file` method from the `FileHandler` class is used to save the content to the files in the `'static/generated/preview/'` folder. This folder is used to serve the generated files in a preview iframe.

### `templates/index.html`

This is the main frontend template for the Website Generator. It contains a form to accept the brief input from the users and shows the mobile and desktop previews of the generated website using iframes.

A button labeled "Switch to desktop view" or "Switch to mobile view" is used to toggle between mobile and desktop previews using JavaScript.

### `static/generated/preview/`

This folder contains the generated `index.html` and `styles.css` files. The files are served by Flask's static file handler, making it possible to display the preview of the generated website within iframes in the `index.html` template.

## Usage Examples

Example 1:

Brief:
"A nature-friendly, eco-conscious boutique hotel chain with properties in stunning locations surrounded by nature. The website should showcase their commitment to sustainability and the unique experiences they provide for guests in a clean, modern design. Use the image from https://source.unsplash.com/300x300/?hotel as an example."

Example 2:
"Generate content and images for a fictional e-commerce platform, 'EcoHome Essentials'. The AI should develop persuasive product descriptions and display visually appealing images of sustainable home products such as eco-friendly cleaning supplies, reusable kitchenware, and energy-efficient appliances. This will help our users make informed decisions while shopping for eco-friendly home solutions."

Example HTML code for random sustainable home product images (300x300):
`<img src="https://source.unsplash.com/300x300/?sustainable-home-products" alt="Random Sustainable Home Product Image">

