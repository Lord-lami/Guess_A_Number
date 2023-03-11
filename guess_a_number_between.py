"""Guessing game
The user guesses a number between the limits
passed to the file when it is run"""

from random import randint
from sys import argv, exit

def getLimitsReturnRandom():
	"""Checks if the input to the file is a number
	and returns a random number to be used for the guessTheNumber function"""
	try:
		left = int(argv[1])
		right = int(argv[2])
		randnum = randint(left, right) if left < right else randint(right, left)
		# in case the user calls the file like this:
		# guess_a_number_between 1 2
		# or
		# guess_a_number_between 2 1
		# The same range will be created
	except ValueError as err:
		print("Pass Numbers Only!")
		print(err)
		return err
	except IndexError as err:
		print("You must pass at least 2 numbers to the file when running it")
		print(err)
		return err
	else:
		return randnum, left, right


def guessTheNumber(randnum_and_limits):
	"""Accepts input from the terminal and compares it with
	the generated random number.
	It allow the user to try again if they get it wrong"""
	if not isinstance(randnum_and_limits[0], int):
		print(f'randnum_and_limits[0]: \'{randnum_and_limits[0]}\' is not an integer')
		return ValueError()
	tries = 0
	while True:
		try:
			guess = int(input(f'Guess a number between {randnum_and_limits[1]} and {randnum_and_limits[2]}> '))
		except ValueError as err:
			print("Pass Numbers Only!")
			print(err)
			continue
			# if isinstance(randnum, int):
			# 	continue
			# else:
			# 	return
		else:
			tries += 1
			if guess == randnum_and_limits[0]:
				if tries == 1:
					print("You guessed the answer in one try. You're a beast!")
				else:
					print(f'Good job! You guessed the anwer in {tries} tries')
				break
			else:
				print("You guessed incorrectly. The answer hasn't changed you can try again")
				continue

if __name__ == '__main__':
	answer = getLimitsReturnRandom()
	guessTheNumber(answer)

# 
