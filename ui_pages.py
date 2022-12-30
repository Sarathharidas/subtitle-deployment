from flask_ngrok import run_with_ngrok
from flask import send_from_directory, send_file
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

from flask import Flask, render_template, request
from tqdm import tqdm

app = Flask(__name__)
run_with_ngrok(app) 

UPLOAD_FOLDER = '/content/upload_video'
ALLOWED_EXTENSIONS = {'mp4'}

app = Flask(__name__)
run_with_ngrok(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file', name=filename))
    return '''
    <!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Add Subtitles to Your Video</title>
    <style>
      /* Add some styling to make the page look beautiful */
      body {
        font-family: sans-serif;
        max-width: 600px;
        margin: 0 auto;
        padding: 30px;
        background: linear-gradient(rgba(255, 255, 255, 0.5), rgba(255, 255, 255, 0.5));
      }

      h1 {
        text-align: center;
        color: #333;
      }

      .instructions {
        margin-top: 30px;
        margin-bottom: 30px;
        color: #333;
      }

      .step {
        margin-bottom: 10px;
      }

      /* Style the form to match the background */
      form {
        background: rgba(255, 255, 255, 0.8);
        padding: 20px;
        border-radius: 5px;
      }

      label {
        display: block;
        margin-bottom: 10px;
      }

      input[type="file"] {
        width: 100%;
      }

      input[type="submit"] {
        background: #333;
        color: white;
        border: none;
        padding: 10px;
        border-radius: 5px;
        cursor: pointer;
      }
    </style>
  </head>
  <body>
    <h1>Add Subtitles to Your Video</h1>
    <div class="instructions">
      <p>To add subtitles to your video, please follow the below steps:</p>
      <div class="step">
        1. Upload your video or audio file. Audio files will be faster
      </div>
      <div class="step">
        2. Get auto-generated subtitles
      </div>
      <div class="step">
        3. Upload the auto-generated subtitles to YouTube, and then edit your subtitles
      </div>
  
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <font size="+5">
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form> </font>
    '''

@app.route('/upload', methods=['POST'])
def upload():
  video = request.files['video']
  video.save('/content/upload_video/video.mp4')
  return 'Video uploaded successfully'

from flask import send_from_directory
import subprocess
import os
import time
@app.route('/uploads/<name>')
def download_file(name):
    command = "ffmpeg -i /content/upload_video/{} -ab 160k -ac 2 -ar 44100 -vn {}.wav".format(name, name)
    subprocess.call(command, shell=True)
    #os.system('whisper "{}.wav" --task translate'.format(name))
    #time.sleep(60)
    #return send_file('/content/{}.wav.srt'.format(name), as_attachment=True)
