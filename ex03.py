from string import punctuation
import sys

def count_spaces(text) -> int:
    spaces = 0
    for i in text:
        if i == ' ':
            spaces += 1
    return spaces


def text_analyzer(*args):
	if len(args) != 1:
		print("ERROR\n")
		exit()
	uppercase = 0
	lowercase = 0
	punc = 0
	spaces = 0
	for i in args[0]:
		if i.isupper():
			uppercase += 1
		elif i.islower():
			lowercase += 1
		elif i in punctuation:
			punc += 1
	data = f" The text contains {len(args[0])}\n - {uppercase} upper letters\n - {lowercase} lower letters\n " \
		   f"- {punc} punctuation marks " \
		   f"\n - {count_spaces(args[0])} spaces "
	return data

result = []
for line in sys.stdin:
	if "Done" == line.rstrip():
		break
	result.append(line)

res = ' '.join(result)
print(text_analyzer(res))
