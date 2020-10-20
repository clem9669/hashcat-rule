#!/usr/bin/env python3

import string

# print(string.digits)
a = """!"#$%&'()*+,-./:;<=>?@[\]^_{|}~"""

# for i in a:
# 	print("$"+i)

for i in string.digits:
	for j in a:
		print("$"+j+" $"+i)

for k in string.digits:
	for i in string.digits:
		for j in a:
			print("$"+j+" $"+i+" $"+k)

for i in string.digits:
	for j in a:
		print("c $"+j+" $"+i)

for k in string.digits:
	for i in string.digits:
		for j in a:
			print("c " +"$"+j+" $"+i+" $"+k)