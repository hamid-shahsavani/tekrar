# arguments used : function, speed, method, output and save function return value ...

# arguments default value : speed = 3 , method = 1

from tekrar import loading

def write_number():
	print('started ...')
	try:
		for i in range(333333):
			a = open('numbers','a')
			a.write(str(i)+'\n')
		return 'finished'
	except:
		return 'error'

value = loading(function = write_number, speed = 4, method = 1, output = False)

if value == 'finished':
	print('process finished ...')
elif value == 'error':
	print('process failed ...')