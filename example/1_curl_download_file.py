# arguments used : method, speed, function, argument , output

# arguments default value : method = 1 , speed = 3 , output = True

from tekrar import loading
from os import system

def download_file(file_name):
	system('curl -SslL https://github.com/sys113/tekrar/archive/master.zip -o {}.zip'.format(file_name))
	print('download completed ...')

loading(function = download_file, argument = ['tekrar'], method = 2, speed = 5 , output = True)