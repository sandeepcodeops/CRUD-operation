"""
the creation for the simple CSV file uploading server
"""
import os
from flask import *
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'D:\\Codeops\\Database Management\\file'
ALLOWED_EXTENSION = 'csv'
""" The required libraries are imported and created a storage path for 
uploaded files and mentioned the allowed extension
"""
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    """
    This function represents the file extension is correct or not
    Input:
        :param filename: input is any file
    Return:
        :return: returns the if file extension is exists not
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSION


@app.route('/')
def upload():
    """
    This function represents the Home page for file uploading
    :return: Home page HTML
    """
    return render_template("file_upload_form.html")


@app.route('/success', methods=['POST'])
def success():
    """
    This function represents the POST method for file uploading
    :return: the file stored in given path and return success page
    """
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template("success.html", name=file.filename)


if __name__ == '__main__':
    app.run(debug=True)
