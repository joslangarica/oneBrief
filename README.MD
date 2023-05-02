# Website Generator Application

This Website Generator Application allows users to generate a simple HTML and CSS code pair based on a text brief. Users input a brief and the application uses OpenAI's GPT-3 model to generate the content. It provides a live preview of the generated website in both mobile and desktop views.

## Structure

The application is structured as follows:

```
.
├── app.py
├── generator.py
├── file_handler.py
├── main.py
├── venv (optional)
├── templates
│   └── index.html
└── static
    └── generated
        └── preview
            ├── index.html
            └── styles.css
```

## Files and Functionalities

### `app.py`

This file contains the main Flask application setup and routing. The application defines a single route `/` with methods `GET` and `POST`. 

When generating a website, the app receives a brief (`POST`), generates the HTML and CSS files for the website, and then stores the files in the `'static/generated/preview/'` folder. The preview URL is passed to the `index.html` template to display the generated website within an iframe in both mobile and desktop views.

### `generator.py`

This file contains the functions for generating the HTML and CSS content using OpenAI's GPT-3. The `generate_html_css` function accepts a text brief and queries GPT-3 to generate the HTML and CSS content. The result is returned as a tuple containing the HTML and CSS code as strings.

### `file_handler.py`

This file contains a single function, `save_to_file`, for saving content to a file. The function accepts the filename, content, and an optional subdirectory. The content is saved to the specified file, optionally within the subdirectory.

### `main.py`

This file is responsible for the main logic of generating the website files. The `generate_website_files` function takes a brief as input and calls the `generate_html_css` function from `generator.py` to produce the HTML and CSS code. 

Then, the `save_to_file` function from `file_handler.py` is used to save the content to files in the `'static/generated/preview/'` folder. This folder is used to serve the generated files in a preview iframe.

### `templates/index.html`

This is the main frontend template for the Website Generator. It contains a form to accept the brief input from the users and shows the mobile and desktop previews of the generated website using iframes.

A button labeled "Switch to desktop view" or "Switch to mobile view" is used to toggle between mobile and desktop previews using JavaScript.

### `static/generated/preview/`

This folder contains the generated `index.html` and `styles.css` files. The files are served by Flask's static file handler, making it possible to display the preview of the generated website within iframes in the `index.html` template.

## How to Run the Program

1. Create a virtual environment (optional) and activate it:
   - `pip install virtualenv`
   - `virtualenv venv`
   - `source venv/bin/activate` (Mac/Linux) or `.\venv\Scripts\activate` (Windows)

2. Install the required dependencies:
   - `pip install Flask openai python-dotenv`

3. Run the Flask application:
   - `python app.py`

4. Visit the URL `http://127.0.0.1:5000/` in a web browser to access the Website Generator page.

## Generating Website Previews

1. Enter a brief for the website in the textarea on the Website Generator page.
2. Click the "Generate Website" button.
3. The generated website preview will be displayed in a mobile-sized container.
4. Click the "Switch to desktop view" button to toggle between mobile and desktop previews.

## Example Brief Promt
"A nature-friendly, eco-conscious boutique hotel chain with properties in stunning locations surrounded by nature. The website should showcase their commitment to sustainability and the unique experiences they provide for guests in a clean, modern design. Use image from https://source.unsplash.com/300x300/?hotel" alt="Random Hotel Image depending on the subject of the website"

## EXAMPLE 2
 generate unique content and images for a fictional e-commerce platform, "EcoHome Essentials". The AI should develop persuasive product descriptions and display visually appealing images of sustainable home products such as eco-friendly cleaning supplies, reusable kitchenware, and energy-efficient appliances. This will help our users make informed decisions while shopping for eco-friendly home solutions.

Example HTML code for random sustainable home product images (300x300):
`<img src="https://source.unsplash.com/300x300/?sustainable-home-products" alt="Random Sustainable Home Product Image">

