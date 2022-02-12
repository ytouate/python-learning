# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex02.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ytouate <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/02/12 10:47:38 by ytouate           #+#    #+#              #
#    Updated: 2022/02/12 10:47:55 by ytouate          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def check_num(x):
	if (x % 2 != 0):
		return "I’m Odd.\n"
	elif (x == 0):
		return "I’m Zero.\n"
	else:
		return "I’m Even.\n"

def myAtoi(string):
	res = 0
	for i in range(len(string)):
		res = res * 10 + (ord(string[i]) - ord('0'))
	return res

def check_arg(string):
	for i in string:
		if (i.isdigit() == False):
			return True

if (len(sys.argv) == 2):
	if (check_arg(sys.argv[1])):
		print("argument is not integer")
		exit()
	print(check_num(myAtoi(sys.argv[1])))
elif (len(sys.argv) == 1):
	exit()
else:
	print("more than one argument is provided\n")
