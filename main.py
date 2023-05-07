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
    html_prompt = f" examine the provided brief '''{brief}''' and write the HTML5 single page website content. The output should include content for all sections. Use Bootstrap for the layout.  Develop the HTML (INCLUDING BUT NOT LIMITING  to:  declaring the appropriate doctype, including HTML5 tags, and adding descriptive metadata, metadescription and keywords). ADD THE CONTENT FOR ALL THE SECTIONS NEEDED. Add link rel stylesheet(style.css) and  add CSS instructions for the CSS designer. The site should contain an adaptative navigation menu with the sections anchors. include a Hero banner with a Subtitle and a CTA button. include an introduction section about the business with photo layout. include a section displaying the business services/products in an engaging way. Add image gallery using images from https://source.unsplash.com/random?relatedkeyword (change the relatedkeyword according to the each section content), include alt attributes showcasing their services/products. Each section of  website content should have  Title tags, subtitles and paragraphs (if theres no content provided, make it up) and IMAGES or graphic elements .  Include a responsive contact form. After you finish, REVIEW  the HTML and make sure it is alligned to SEO and UX.  Your final submission should include  ONLY the HTML (with all the sections described above and in the brief) code (with all the information of the website). Please do not add extra comments besides the website HTML content."

    html_content = generate_content(html_prompt, api_key)
    print(html_content)

    # Generate CSS content using the HTML content
    print("Generating CSS content...")
    css_prompt = f"review the provided '''{html_content}''', and write responsive CSS code using Bootstrap. Enhance the website's visual experience with  animations, galleries, parallax effects among others. Make sure the content and images are  justified and theres NO overlap.  Upon completion,  review  the  CSS code and ensure it is fully responsive (no content overlap and justified). Your final submission  should ONLY contain  the CSS CODE, without any additional comments."

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
