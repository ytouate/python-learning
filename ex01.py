# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    py.py                                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ytouate <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/02/11 11:07:52 by ytouate           #+#    #+#              #
#    Updated: 2022/02/11 11:08:41 by ytouate          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
 import sys

def func(string):
	return (string[::-1])

result = []
for j in sys.argv[::-1]:
	result.append(func(j).swapcase())

s = ' '
result.pop(len(result) - 1)
string = s.join(result)
print (string)
