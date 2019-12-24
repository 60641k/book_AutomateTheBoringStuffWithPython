
def collatz(number):
	global x
	if number % 2 == 0:
		print(number // 2)
		x = number // 2
		return x
	else:
		print(3*number + 1)
		x = 3*number + 1
		return x


while True:
	try:
		x = int(input('Please enter number: '))
	except ValueError: 
		print('ValueError: You must enter an integer!')
		continue
	break
	
while x != 1:
	collatz(x)
	

