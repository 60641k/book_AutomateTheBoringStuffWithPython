def commas(lst):
	output = ''
	if len(lst) == 0:
		print('The list is empty')
	elif len(lst) == 1:
		print(lst[0])
	else:
		for i in range(len(lst) - 1):
			if i != len(lst) - 2: 
				output += lst[i]+', '
			else:
				output += lst [i]+' '
		output += 'and '+lst[-1]
	print(output)

mylist = ['apples', 'tofu', 'cats', 'bees', 'ggs']



print(mylist, len(mylist))

commas(mylist)


