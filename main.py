import os
from dotenv import load_dotenv
from generator import generate_content
from file_handler import save_to_file

def generate_website_files(brief):
    # Load environment variables from .env file
    load_dotenv()

    # Set OpenAI API key
    api_key = os.getenv("OPENAI_API_KEY")

    # Generate HTML content
    print("Generating HTML content...")
    html_prompt = f"  create an HTML file based on the provided brief,  the CSS will be written separately after the HTML is delivered so write the html considering that(include the link rel stylesheet to style.css). the HTML code should declare the appropiate doctype, incorporate the HTML tags (h1...h6), metadata, set appropiate title tags, images should have alt attribute, descriptive meta attributes, with the proper document structure, group relevant sections, Include all necessary elements (tags, titles, headers, alt attributes, paragraphs, images, etc.) for SEO Best Practices, if necessary Use image placeholders from [https://source.unsplash.com](https://source.unsplash.com/) . Remember that your answer should only contain the HTML code with no additional comments from you. {brief}"
    html_content = generate_content(html_prompt, api_key)

    # Generate CSS content using the HTML content
    print("Generating CSS content...")
    css_prompt = f"Please analyze the provided html and write CSS responsive alligned to the brief (make sure the nav adapts accordingly). Your CSS code should: Be well-commented, it should work and display properly on mobile, desktop and tablet.Include basic animations or dynamic. Use image placeholders from [https://source.unsplash.com](https://source.unsplash.com/) if necessary. Remember that your answer should only contain the CSS code with no additional comments from you {brief}"
    css_content = generate_content(css_prompt, api_key, conversation_history=[
        {"role": "user", "content": html_prompt},
        {"role": "assistant", "content": html_content}
    ])

    # Save the HTML and CSS content to local files
    save_to_file("index.html", html_content)
    save_to_file("style.css", css_content)
    return True

    # Save the HTML and CSS content to local files inside the static/generated/preview folder
    save_to_file("index.html", html_content, subdir="static/generated/preview")
    save_to_file("styles.css", css_content, subdir="static/generated/preview")

if __name__ == "__main__":
    brief = input("Enter a brief for the website: ")
    generate_website_files(brief)
