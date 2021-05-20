from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import argparse
# import wget
import shlex, subprocess

import pdb





class MyAppFembed():
    def __init__(self):
        # pdb.set_trace()
        parser = argparse.ArgumentParser()
        parser.add_argument("-c", "--calidad", help="Nombre de id De Google Drive")
        parser.add_argument("-L", "--link", help="url fembed a descargar")
        args = parser.parse_args()
        
        # "https://www.fembed.com/f/pwdd1im81nq068r"
        # Aquí procesamos lo que se tiene que hacer con cada argumento
        if args.link:
            self.url_inicial = args.link
            self.resp = requests.get(self.url_inicial)
            self.soup = BeautifulSoup(self.resp.content, 'html.parser')
            self.title = self.soup.title.text.replace(" - Free download", "")
            
            print(self.title)
            self.url_api_final = self.resp.url.replace("/f/", "/api/source/")
            self.r = requests.post(self.url_api_final).json()
            
            
            for i in self.r["data"]:
                if i["label"] == "720p":
                    # print(i["file"])
                    # wget.download(i["file"], '.'+self.title)
                    linkk = 'aria2c -x16 -s16 "'+i["file"]+'" -o "'+self.title+'"'
                    print(linkk)
                    # input()
                    subprocess.call(shlex.split(linkk))
                    print("File Downloaded")
                    print()

MyAppFembed()
