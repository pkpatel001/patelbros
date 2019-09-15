#!/usr/bin/python3.7
# syntax.py by Bill Weinman <http://bw.org/>
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copywrite (c) 2010 The BearHeart Group, LLC

class egg:
    def __init__(self, kind = "Fried"):
        self.kind = kind

    def whatKind(self):
        return self.kind

def main():
    fried = egg()
    scrambled = egg('scrambled')
    print(scrambled.whatKind())

if __name__ == "__main__": main()