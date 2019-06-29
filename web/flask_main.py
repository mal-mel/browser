from flask import Flask, request, render_template, jsonify, send_from_directory
import os
from datetime import datetime


UPLOAD_FOLDER = os.path.join('uploads')
app = Flask(__name__, static_url_path='/static/')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        file = request.files['img']
        filename = datetime.now()
        file.save(f'uploads/{filename}')
        return jsonify({'files': f'<a href="uploads/{filename}">{filename}</a><br>'})
    return render_template('main.html', files=os.listdir('uploads/'))


@app.route('/uploads/<filename>/', methods=['GET'])
def file_page(filename):
    if filename in os.listdir('uploads/'):
        return render_template('file.html', file=os.path.join(app.config['UPLOAD_FOLDER'], filename))
