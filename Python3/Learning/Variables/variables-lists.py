#!/usr/bin/python3.7
# variables.py by Bill Weinman <http://bw.org/>
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copywrite (c) 2010 The BearHeart Group, LLC

def main():
    x = (1, 2, 3)
    y = [1, 2, 3]
    z = 'string'
    a = 'string'
    b = 'string'
    c = (1, 2, 3, 4, 5)
    for i in c:
        print(i)
    d = "string"
    for j in d:
        print(j)
    y.append(5)
    y.insert(2, 7)
    print(type(x), x)
    print(type(y), y)
    print(type(z), z)
    print(type(a), a[2])
    print(type(b), b[2:4])
    
if __name__ == "__main__": main()