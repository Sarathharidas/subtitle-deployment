
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('contact.html')



# @app.route('/', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         # check if the post request has the file part
#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
#         file = request.files['file']
#         # If the user does not select a file, the browser submits an
#         # empty file without a filename.
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)
#         if file:
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             return redirect(url_for('download_file', name=filename))
#     return '''
#     <!doctype html>
#     <title>Upload new File</title>
#     <h1>Upload new File</h1>
#     <form method=post enctype=multipart/form-data>
#       <input type=file name=file>
#       <input type=submit value=Upload>
#     </form>
#     '''

# @app.route('/uploads/<name>')
# def download_file(name):
#     command = "ffmpeg -i /home/sarathharidas13/app/video_upload/{} -ab 160k -ac 2 -ar 44100 -vn {}.wav".format(name, name)
#     subprocess.call(command, shell=True)
#     os.system('whisper "{}.wav" --task translate'.format(name))
#     #time.sleep(60)
#     return send_file('/home/sarathharidas13/app/video_upload/{}.wav.srt'.format(name), as_attachment=True)


if __name__ == '__main__':
  app.debug
  app.run()