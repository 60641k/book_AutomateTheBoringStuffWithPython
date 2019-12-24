#!usr/bin/env python3

while True:
	print('Who are you?')
	name = input()
	if name != 'Joe':
		continue
	print('Hello, Joe. What is the password? (It is a fish.)')
	password = input()
	while password != 'swordfish':
		print('Access denied.')
		password = input()
	break
print('Access granted.')