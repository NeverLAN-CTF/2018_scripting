#!/usr/bin/python2.7

import json

with open('even_more_numbers_with_some_mild_inconveniences.txt', 'r') as infile:
        sum = 0
        for line in infile:
                cleanish_line = line.replace(","," ")
                clean_line = cleanish_line.split()
                for value in clean_line:
                        try:
                                sum = sum + int(value)
                        except:
                                pass
        print sum
