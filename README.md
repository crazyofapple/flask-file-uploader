# file-uploader
user python 2.7 and flask to create a API that can upload and download files

# prepare
python 2.7
pip install requests
pip install argparse

# start api
pyton app.py -p 80

# test api
python test.py -s 127.0.0.1:80 -u /your/file/path
python test.py -s 127.0.0.1:80 -d filename -f /your/target/folder
