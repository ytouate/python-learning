# kata00

t = (19,42,21)
print(f"The {len(t)} numbers are {t[0]}, {t[1]}, {t[2]}")

# kata01
languages = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

for key in languages:
	print(f"{key} was created by {languages[key]}")

#kata02
t = (3,30,2019,9,25)
print(f"{t[-2]}/{t[-1]}/{t[-3]} 0{t[0]}:{t[1]}")

#kata03
phrase = "The right format"
string = []
for i in range(42):
	string.append('-')
string.append(phrase)
result = ''.join(string)
print(result)

#kata04
t = ( 0, 4, 132.42222, 10000, 12345.67)
n = "{:.2e}".format(t[3])
p = "{:.2e}".format(t[4])
print(f"module_0{t[0]}, ex_0{t[1]}, : {round(t[2], 2)}, {n}, {p}")
