import os
import urllib.request
from flask import Flask, flash, request, redirect, render_template, jsonify
from werkzeug.utils import secure_filename
import random
import string

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

UPLOAD_FOLDER = 'uploads'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


def randomStringDigits(stringLength=6):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

def allowed_file(filename):
    return '.' in filename # and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def upload_form():
    return render_template('upload.html')


@app.route('/action', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            return extract_info(filename)
        else:
            flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
            return redirect(request.url)

def downloadFromdb(userid, filename):
    data = f"Hi {userid} {filename}"
    return data

def upload2db(logdata):
    #userid = randomStringDigits()
    userid = 111111
    print("Try to Insert")
    db.logs.insert_one({'id': userid, 'log': logdata})
    print("Inserted into DB")

    return userid

def run_aws(filename):
    data = f"AWS {filename}"
    
    # place dynamic analysis here
    
    with open("output.txt", "r") as file:
        data = file.read() #.replace('\n','<br>')
    return data

def extract_info(filename):
    data = "None"
    try:
        data = run_aws(filename)
        #userid = upload2db(logdata)
        #data = downloadFromdb(userid, filename)

    except Exception as e:
        data = f"Error Occured: {e}"
        return render_template("results.html", data=data)

    return render_template("results.html", data=data)

@app.route("/results")
def results():
    return render_template("results.html")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/home')
def home():
    return render_template('upload.html')


if __name__ == "__main__":
    app.run()
