import random

def is_int(string):
	try:
		int (string)
		return True
	except ValueError:
		return False

def man():
	man = '''This is an interactive guessing game!
	You have to enter a number between 1 and 99 to find out the secret number.
	Type 'exit' to end the game
	Good luck!'''
	return (man)

def msg():
	msg = '''The answer to the ultimate question of life,
	the universe and everything is 42.'''
	return (msg)
def main():
	is_on = True
	attempts = 0
	number = random.randint(1, 99)
	print(man())
	while is_on:
		choice = input("What's your guess between 1 and 99?\n")
		# checking the player input #
		if choice == "exit":
			print("Goodbye!")
			is_on = False
		elif is_int(choice):
			n = int(choice)
		else :
			print("This is not an integer")
		# checking if the number within the correct range #
		if n < 1 or n > 99:
			print("Please insert the number withing the asked range")

		# checking for the number #
		if n == number:
			if n == 42:
				print(msg())
			if attempts == 0:
				print("Congratulations! You got it on your first try!")
				return 
			print(f"Congratulations, you've got it!\n")
			print(f"You won in {attempts} attempts!")
			is_on = False
		elif n > number:
			print("Too high !")
			attempts += 1
		else :
			attempts += 1
			print("Too low !")
main()
	
	
