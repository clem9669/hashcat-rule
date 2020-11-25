#!/usr/bin/env python3

import string

# print(string.digits)
a = """!"#$%&'()*+,-./:;<=>?@[\]^_{|}~1234567890"""

# for i in a:
# 	print("$"+i)

# for i in string.digits:
# 	for j in a:
# 		print("$"+j+" $"+i)

# for k in string.digits:
# 	for i in string.digits:
# 		for j in a:
# 			print("$"+j+" $"+i+" $"+k)

# for i in string.digits:
# 	for j in a:
# 		print("c $"+j+" $"+i)

# for k in string.digits:
# 	for i in string.digits:
# 		for j in a:
# 			print("c " +"$"+j+" $"+i+" $"+k)

for j in string.ascii_letters:
	for i in a:
		print("$"+j+" $"+i)

for j in string.ascii_letters:
	for i in a:
		print("c $"+j+" $"+i)

for j in string.ascii_letters:
	for i in a:
		print("u $"+j+" $"+i)