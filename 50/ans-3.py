#!/usr/bin/python2.7

import json

with open('some_more_numbers.txt', 'r') as infile:
	sum = 0
	for number in infile:
		sum += int(number)

	print sum	
	
