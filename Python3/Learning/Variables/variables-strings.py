#!/usr/bin/python3.7
# variables.py by Bill Weinman <http://bw.org/>
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copywrite (c) 2010 The BearHeart Group, LLC

def main():
    n1 = 42
    s1 = 'This is a string!'
    s2 = "This is also\n a string!"
    s3 = r"This is also\n a string!"
    s4 = "This is a {} string!".format(n1)
    s5 = '''\
    this is also a string,
    a very long text of,
    more text!!!
    '''
    print(s1)
    print(s2)
    print(s3)
    print(s4)
    print(s5)

if __name__ == "__main__": main()