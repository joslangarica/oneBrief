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
    html_prompt = f"write an optimized html file that follows SEO and UX best practices for the following brief: {brief}"
    html_content = generate_content(html_prompt, api_key)

    # Generate CSS content using the HTML content
    print("Generating CSS content...")
    css_prompt = f"write a responsive, modern look css file for the following brief: {brief}"
    css_content = generate_content(css_prompt, api_key, conversation_history=[
        {"role": "user", "content": html_prompt},
        {"role": "assistant", "content": html_content}
    ])

    # Save the HTML and CSS content to local files
    save_to_file("index.html", html_content)
    save_to_file("styles.css", css_content)
    return True

if __name__ == "__main__":
    brief = input("Enter a brief for the website: ")
    generate_website_files(brief)
