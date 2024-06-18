from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
import os

app = Flask(__name__)


def create_static_folder():
    static_folder = os.path.join(app.root_path, 'static')
    if not os.path.exists(static_folder):
        os.mkdir(static_folder)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file:
        
        create_static_folder()

        
        img = Image.open(file)

        
        input_file = os.path.join(app.root_path, 'static', 'input.png')
        img.save(input_file)

        
        img_pixel_art = img.resize((img.width // 10, img.height // 10), Image.NEAREST)
        img_pixel_art = img_pixel_art.resize((img_pixel_art.width * 10, img_pixel_art.height * 10), Image.NEAREST)

        
        output_file = os.path.join(app.root_path, 'static', 'output.png')
        img_pixel_art.save(output_file)

        return render_template('result.html', input_file=input_file, output_file=output_file)

if __name__ == '__main__':
    app.run(debug=True)
