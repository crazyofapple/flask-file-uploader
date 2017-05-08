import requests
import os
import argparse

class file_uploader():
    def __init__(self, ip):
        self.web = 'http://{0}'.format(ip)

    def upload(self, file_path, key):        
        url = '{0}/upload?key={1}'.format(self.web, key)            
        files = {'file': open(file_path, 'rb')}            
        response = requests.post(url, files = files)           
        json_response = response.json()
        print json_response

    def download(self, file_name, target_folder):
        url = '{0}/download/{1}'.format(self.web, file_name)    
        req = requests.get(url)        
        with open(os.path.join(target_folder, file_name), 'wb') as file:
            file.write(req.content)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()    
    parser.add_argument("-s", "--server", help="server ip address", type=str, required=True)  
    #upload
    parser.add_argument("-u", "--uploadfile", help="upload file pth", type=str, required=False)  
    parser.add_argument("-k", "--uploadkey", help="upload key (password)", type=str, required=False)  

    #download
    parser.add_argument("-d", "--downloadfile", help="download file name", type=str, required=False)  
    parser.add_argument("-f", "--downloadfolder", help="download file local folder", type=str, required=False)  
    
    args = parser.parse_args()
    
    sa = file_uploader(args.server)
    if args.uploadfile:
        sa.upload(args.uploadfile, args.uploadkey)
    if args.downloadfile and args.downloadfolder:
        sa.download(args.downloadfile, args.downloadfolder)

        