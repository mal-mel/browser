from flask import Flask, request, render_template, jsonify, url_for
from werkzeug.wsgi import SharedDataMiddleware
import os
from datetime import datetime

UPLOAD_FOLDER = os.path.join('uploads')
app = Flask(__name__, static_url_path='/static/')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.add_url_rule('/uploads/<filename>', 'uploaded_file',
                 build_only=True)
app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
    '/uploads': app.config['UPLOAD_FOLDER']
})


@app.route('/', methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        file = request.files['img']
        filename = datetime.now()
        file.save(f'uploads/{filename}')

        response = (f'<div class="col-md-3">\n'
                    f'				<a href="/uploads/{filename}" style="text-decoration: none;">\n'
                    f'					<div class="card text-center" style="width: 300px; height: 70px; margin-bottom: 10px;">\n'
                    f'						<div class="card-body">\n'
                    f'							<span>{filename}</span>\n'
                    f'						</div>\n'
                    f'					</div>\n'
                    f'				</a>\n'
                    f'			</div>')
        return jsonify({'files': response})
    return render_template('main.html', files=os.listdir('uploads/'))


@app.route('/uploads/<filename>/', methods=['GET'])
def file_page(filename):
    if filename in os.listdir('uploads/'):
        return render_template('file.html', file=url_for('uploaded_file', filename=filename))
    return render_template('main.html', files=os.listdir('uploads/'))
