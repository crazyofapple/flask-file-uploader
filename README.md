# file-uploader
user python 2.7 and flask to create a API that can upload and download files

Installation
------------
install python 2.7 first

    pip install flask
    pip install requests
    pip install argparse

Usage
------------
start your API

    python app.py -p 80

Test
------------
upload

    python test.py -s "127.0.0.1:80" -u "/your/file/path"

download

    python test.py -s "127.0.0.1:80" -d "filename" -f "/your/target/folder"
