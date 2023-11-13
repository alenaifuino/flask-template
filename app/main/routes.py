import os

from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from . import main

@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html')

@main.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        # Handle error
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        # Handle error
        return redirect(request.url)
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(main.config['MEDIA_FOLDER'], filename))
        return redirect(url_for('uploaded_file', filename=filename))

@main.app_errorhandler(400)
def bad_request_error(error):
    return render_template('400.html'), 400

@main.app_errorhandler(403)
def forbidden_error(error):
    return render_template('403.html'), 403

@main.app_errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@main.app_errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500