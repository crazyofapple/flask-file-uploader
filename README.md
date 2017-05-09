# file-uploader
user python 2.7 and flask to create a API that can upload and download files

Installation
------------
install python 2.7 first

    pip install flask
    pip install requests
    pip install argparse
    pip install random

Usage
------------
start your API (port=80)

    python app.py -p 80
    
start your API with upload password(key="test")

    python app.py -p 80 -k test
    
if you want to run on background
    
    nohup python /your/path/file-uploader/app.py -p 80 &

kill backgorund process

    ps -ef
    kill {PID}

Test
------------
upload

    python test.py -s "127.0.0.1:80" -u "/your/file/path"

upload with password(key)

    python test.py -s "127.0.0.1:80" -u "/your/file/path" -k "yourkey"
    
response json:
    
- {'url': '/download/jzssxhmzyr58fuaase9wuck7xmkrlq3o2kb1pq7isdjb4woiu09elsuap9s98y9e', 'result': True}

download

- get random key from response (jzssxhmzyr58fuaase9wuck7xmkrlq3o2kb1pq7isdjb4woiu09elsuap9s98y9e)

python test.py -s "127.0.0.1:80" -d "random_key_from_upload_response" -f "/your/local/folder"
