#!/usr/bin/python3.7
# syntax.py by Bill Weinman <http://bw.org/>
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copywrite (c) 2010 The BearHeart Group, LLC

def main():
    a, b = 2, 1
    s = "Less than" if a < b else "not less than"
    if a < b:
        print("a is less than b")
        print(s)
    elif a > b:
        print("a is greater than b")
        print(s)
    else:
        print("a is equal to b")
        print(s)
    
if __name__ == "__main__": main()