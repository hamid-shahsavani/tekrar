from tekrar import loading
from os import system

def download_file():
	system('curl -Ss https://github.com/sys113/tekrar/archive/master.zip')

loading(function = download_file , method = 1 , speed = 2)
