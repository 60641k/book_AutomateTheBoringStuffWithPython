import random

tmpstr = ''
for i in range(100):
	if random.randint(0,1) == 0:
		tmpstr += 'T'
	else:
		tmpstr += 'H'
print(tmpstr)
print('Tx6: ', tmpstr.count('TTTTTT'))
print('Hx6: ', tmpstr.count('HHHHHH'))