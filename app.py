from flask import Flask, render_template, request, send_from_directory, url_for
from main import generate_website_files
import os
from werkzeug.utils import secure_filename
from flask import send_from_directory


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    preview_url = None
    preview_available = False

    if request.method == 'POST':
        brief = request.form.get('brief')
        if brief:
            files_created = generate_website_files(brief)
            if files_created:
                preview_url = url_for('static', filename='generated/preview/index.html')
                preview_available = True

    return render_template('index.html', preview_url=preview_url, preview_available=preview_available)

@app.route('/download/<filename>')
def download_file(filename):
    try:
        return send_from_directory(os.path.join("static", "generated", "preview"), filename, as_attachment=True)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)