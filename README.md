# file-uploader
user python 2.7 and flask to create a API that can upload and download files

Installation
------------
.. code-block:: bash
python 2.7
pip install requests
pip install argparse

Usage
------------
start your API
.. code-block:: bash
pyton app.py -p 80

Test
------------
upload
python test.py -s 127.0.0.1:80 -u /your/file/path

download
python test.py -s 127.0.0.1:80 -d filename -f /your/target/folder
