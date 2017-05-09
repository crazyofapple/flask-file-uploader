# file-uploader
user python 2.7 and flask to create a API that can upload and download files

- if you don't want everyone can upload file, you can set password.
- download url is random, only the uploader can know the download url.
- provide test.py to upload and downlad easily.

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

get random key from response

- example: jzssxhmzyr58fuaase9wuck7xmkrlq3o2kb1pq7isdjb4woiu09elsuap9s98y9e

download:

    python test.py -s "127.0.0.1:80" -d "random_key_from_upload_response" -f "/your/local/folder"

download by browser

- get url from response json
- example: http://{your ip}:{your port}/download/jzssxhmzyr58fuaase9wuck7xmkrlq3o2kb1pq7isdjb4woiu09elsuap9s98y9e
- just paste on this url on your browser


