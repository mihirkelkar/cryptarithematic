#!/usr/bin/python
import itertools
import string
import re
import sys
#------------------------------------------------------------------------------------------------------------------------------------#
#		ATTENTION !!!!!  : ALL OUTPUTS ARE PRINTED TO A FILE CALLED SENDMOREMOENY.TXT WHICH AUTOMATICALLY GETS CREATED IN THE PWD.
#____________________________________________________________________________________________________________________________________#
fp = open('sendmoremoney.txt', 'w')
sys.stdout = fp
puzzles = ['SEND + MORE == MONEY', 'NEW + YORK == CITY', 'HEAT + WATER == HUMID', 'GOOD + GUY == GREG']

def find(puzzle):
	stuff = re.findall('[A-Za-z]+', puzzle)
	print stuff
	letters  = list(set(''.join(stuff)))
	print letters
	assert len(letters) <= 10
	starts = []
	for term in stuff:
		if term[0] in starts:
			continue
		else:
			starts.append(term[0])
	letters.sort()
	for i in starts:
		letters[:] = [x for x in letters if x != i]
	letters = ''.join(starts) + ''.join(letters)
	start_len = len(starts)
	letters_len = len(letters)
	for j in itertools.permutations('0123456789', len(letters)):
		if '0' not in j[:start_len]:
			temp  = string.maketrans(letters, ''.join(j))
			answer = puzzle.translate(temp)
			try: 
				if eval(answer):
					print(answer)
			except ArithmeticError:
				pass
		
for i in puzzles:
	print i
	find(i)
