# Finding Duplicate characters
from collections import Counter

def find_dup_char(input):
	WC = Counter(input)
	j = -1

	for i in WC.values():
		j = j + 1
		if( i > 1 ):
			print WC.keys()[j],


input = 'geeksforgeeks'
find_dup_char(input)