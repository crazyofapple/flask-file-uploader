import os
import argparse
from flask import Flask, request, redirect, url_for, jsonify, send_from_directory
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'zip'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 1024 #1GB
#app.debug = True

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:         
            return jsonify({'result': False, 'message': 'no file'})         
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':            
            return jsonify({'result': False, 'message': 'no file name'})
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                os.mkdir(app.config['UPLOAD_FOLDER'])
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return jsonify({'result': True, 'url':'/upload/{0}'.format(filename)})

@app.route('/download/<path:filename>', methods=['GET', 'POST'])
def download_file(filename):    
    uploads =  app.config['UPLOAD_FOLDER']    
    return send_from_directory(directory=uploads, filename=filename, as_attachment=True)    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()    
    parser.add_argument("-p", "--port", help="port", type=int, required=False, default=5000)
    parser.add_argument("-s", "--server", help="host", type=str, required=False, default='0.0.0.0')
    args = parser.parse_args()
       
    app.run(host=args.server, port=args.port)                                