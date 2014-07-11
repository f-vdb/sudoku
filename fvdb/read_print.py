#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import logging

# loglevel - comment out the next line and you will see loggings
# logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)



def usage():
    print("usage ./sudoku.py name_der_sudoku_datei.txt")


def printPitch():
    for i in xrange(9):
        print("\n\t", end="")
        for j in xrange(9):
            print(pitch[i][j], " ", end='')
    print("\n") 

"""
def slurpFileToPitch(filename):
    try:
        with open(filename) as f:
            logging.debug("file " + filename + " exists")
            for i in xrange(9):
                for j in xrange(9):
                    c = f.read(1)
                    if(c=='\n'):
                        c = f.read(1)
                    pitch[i].append(int(c))

"""

def slurpFileToPitch(filename, sep='\n'):
    # linksassoziativ nicht wie in Haskell....          
    # lesen, whitespaces vorne und hinten abschneiden,
    # Liste erstellen durch Trennen mit sep
    return open(filename).read().strip().split(sep)



if __name__ == "__main__":
    solution = 0
    pitch = [[],[],[],[],[],[],[],[],[]]
    n = len(sys.argv)
    if n == 1 or n > 2:
        usage()
        exit()
    else:
        print(slurpFileToPitch(sys.argv[1]))


