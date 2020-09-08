'''
Scenario
Let's play a game. We will give you two strings: one being a word (e.g., "dog") and the second being a combination of any characters.
Your task is to write a program which answers the following question: are the characters comprising the first string hidden inside the second string?

For example:
if the second string is given as "vcxzxduybfdsobywuefgas", the answer is yes;

if the second string is "vcxzxdcybfdstbywuefsas", the answer is no (as there are neither the letters "d", "o", or "g", in this order)

Hints:
you should use the two-argument variants of the pos() functions inside your code;
don't worry about case sensitivity.
Test your code using the data we've provided.

Test data
Sample input:
donor
Nabucodonosor

Sample output:
Yes

Sample input:
donus
Nabucodonosor

Sample output:
No
'''
word = input("Enter the word you wish to find: ").upper()
strn = input("Enter the string you wish to search through: ").upper()

found = True
start = 0

for ch in word:
	pos = strn.find(ch, start)
	print(pos)
	if pos < 0:
		found = False
		break
	start = pos + 1
if found:
	print("Yes")
else:
	print("No")
