import random


numberOfStreaks = 0
biglst = []


for experimentNumber in range(10000):
	tmpstr = ''
	for i in range(100):
		if random.randint(0,1) == 0:
			tmpstr += 'T'
		else:
			tmpstr += 'H'

	biglst.append(tmpstr)
	numberOfStreaks += tmpstr.count('TTTTTT') + tmpstr.count('HHHHHH')

print('Number of Streaks of 6 heads or tails: ', numberOfStreaks)

print('Chance of streak: ', numberOfStreaks / 10000)

