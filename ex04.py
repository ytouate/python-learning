import sys

def add(x, y):
	return (x + y)

def substract(x, y):
	return (x - y)

def divide(x, y):
	if (y == 0):
		exit()
	return (x / y)

def multiply(x, y):
	return (x * y)

def remainder(x, y):
	return (x % y)
def atoi(x):
	result = 0
	for i in x:
		result = result * 10 + ord(i)
	return (result)

def is_valid(x):
	return x.isdigit()

def main():
	if len(sys.argv) > 3:
		print("too many arguments")
		exit()
	elif len(sys.argv) < 3:
		print("too few arguments")
	else :
		if is_valid(sys.argv[1]) and is_valid(sys.argv[2]):
			x = int(sys.argv[1])
			y = int(sys.argv[2])
			print(f"sum: {add(x, y)}")
			print(f"Difference: {substract(x, y)}")
			print(f"Product: {multiply(x, y)}")
			if (y != 0):
				result = divide(x, y)
				modulo = remainder(x, y)
			else:
				result = "ERROR (div by zero)"
				modulo = "ERROR (modulo by zero)"
			print(f"Qutient: {result}")
			print(f"Remainder: {modulo}")
		else :
			print("invalid arguments")

main()
