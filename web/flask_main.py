from flask import Flask, request, render_template, url_for

app = Flask('upload')


@app.route('/', methods=['GET', 'POST'])
def main_page():
    url_for('static', filename='css/style.css')
    url_for('static', filename='js/script.js')

    if request.method == 'POST':
        return f'{request.files}'
    return render_template('main.html')
