#!/usr/bin/python3.7
# variables.py by Bill Weinman <http://bw.org/>
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copywrite (c) 2010 The BearHeart Group, LLC

def main():
    num1 = 42
    num2 = 42.0
    num3 = 42 / 9
    num4 = 42 // 9
    num5 = round(42 /9)
    num6 = round(42 /9, 2)
    num7 = 42 % 9
    num8 = int(42.9)
    num9 = float(42)
    print(type(num1), num1)
    print(type(num2), num2)
    print(type(num3), num3)
    print(type(num4), num4)
    print(type(num5), num5)
    print(type(num6), num6)
    print(type(num7), num7)
    print(type(num8), num8)
    print(type(num9), num9)

if __name__ == "__main__": main()