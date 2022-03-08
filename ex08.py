import sys

CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }

def convert(string):
	converted_str = []
	for i in string:
		if i.isalnum() or i == ' ':
			if i == ' ':
				converted_str.append(' / ')
			else:
				converted_str.append(CODE[i.upper()])
		else :
			print("Error")
			exit()
	converted_str = ''.join(converted_str)
	return (converted_str)

def main():
	result = []
	if len(sys.argv) < 2:
		print("invalid args")
		return
	for i in sys.argv[1::]:
		result.append(convert(i))
		result.append(' / ')
	result = ''. join(result)
	print(result)

main()
