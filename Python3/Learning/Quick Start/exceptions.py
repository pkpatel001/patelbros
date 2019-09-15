#!/usr/python3
# exceptions.py by Bill Weinman <http://bw.org/>
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copywrite (c) 2010 The BearHeart Group, LLC

try:
	fh = open('xlines.txt')
	for line in fh.readlines():
		print(line)

except IOError as e:
	print("something bad happened ({})".format(e))

print("after badness")