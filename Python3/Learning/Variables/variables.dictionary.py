#!/usr/bin/python3.7
# variables.py by Bill Weinman <http://bw.org/>
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copywrite (c) 2010 The BearHeart Group, LLC

def main():
    d = dict(
        one = 1, two = 2, three = 3, four = 4, five = 'five'
    )
    d['seven'] = 7
    for k in sorted(d.keys()):
        print(k, d[k])

if __name__ == "__main__": main()