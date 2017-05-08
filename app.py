import os
import argparse
from flask import Flask, request, redirect, url_for, jsonify, send_file
from werkzeug.utils import secure_filename
import random
import string
import json

from datetime import datetime

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'zip'])
UPLOAD_PASSWORD = None
KEY_FOLDER = 'keys'
KEY_LEN = 64

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 1024 #1GB
app.debug = True

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def id_generator(size=256, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # error password
        if UPLOAD_PASSWORD and UPLOAD_PASSWORD != request.args.get('key'):
            return jsonify({'result': False, 'message': 'error key'})         
        
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

            # get randome key
            key = id_generator(size=KEY_LEN)
            target_folder = os.path.join(UPLOAD_FOLDER, key[0:1], key[1:2], key[2:3], key[3:4], key[4:5])
            key_folder = os.path.join(KEY_FOLDER, key[0:1], key[1:2], key[2:3], key[3:4], key[4:5])

            # create folder if not existed
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)
            if not os.path.exists(key_folder):
                os.makedirs(key_folder)

            # save file
            file_path = os.path.join(target_folder, key)
            file.save(file_path)

            # save file info
            with open(os.path.join(key_folder, key), 'w') as keyfile:
                fileinfo = {'filename': filename, 'filepath': file_path, 'uploadon': str(datetime.utcnow())}
                keyfile.write(json.dumps(fileinfo))
            
            return jsonify({'result': True, 'url':'/download/{0}'.format(key)})

@app.route('/download/<path:key>', methods=['GET', 'POST'])
def download_file(key):    
    if len(key) == KEY_LEN:
        #read filename by key
        
        key_file = os.path.join(KEY_FOLDER, key[0:1], key[1:2], key[2:3], key[3:4], key[4:5], key)
        if os.path.exists(key_file):

            # read file name
            with open(key_file) as data_file:    
                data = json.load(data_file)
                filename = data['filename']
                filepath = data['filepath']

            if os.path.exists(filepath):
                return send_file(filename_or_fp = filepath, attachment_filename = filename, as_attachment = True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()    
    parser.add_argument("-p", "--port", help="port", type=int, required=False, default=5000)
    parser.add_argument("-s", "--server", help="host", type=str, required=False, default='0.0.0.0')
    parser.add_argument("-k", "--key", help="upload key (password)", type=str, required=False)
    
    args = parser.parse_args()       

    if args.key:
        UPLOAD_PASSWORD = args.key
    
    app.run(host=args.server, port=args.port)                                