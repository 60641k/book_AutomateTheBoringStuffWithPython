# This is a guess the number game.
import random


print('Enter the X number for range(1 to X):')
xrange = int(input())
secretNumber = random.randint(1, xrange)
print('I am thinking of a number between 1 and ' + str(xrange) + '.')

# Ask the player to guess 7 times.
print('You have 7 tries.')
for guessesTaken in range(1, 8):
	print('Take a guess.')
	guess = int(input())
	if guess < secretNumber:
		print('Your guess is too low.')
	elif guess > secretNumber:
		print('Your guess is too high.')
	else:
		break

if guess == secretNumber:
	print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
	print('Nope. The number I was thinking of was ' + str(secretNumber))