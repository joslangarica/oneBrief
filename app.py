from flask import Flask, render_template, request, send_from_directory
from main import generate_website_files

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        brief = request.form.get('brief')
        if brief:
            files_created = generate_website_files(brief)
            if files_created:
                return send_from_directory(directory='.', filename='index.html', as_attachment=True)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)