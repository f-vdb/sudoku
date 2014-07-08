#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from __future__ has to be the first line 
from __future__ import print_function
import sys
import logging

# loglevel - comment out the next line and you will see loggings
# logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


def check(x, y, wert):
    if(checkHorizontal(y, wert)):
        return 1
    if(checkVertikal(x, wert)):
        return 1
    if(checkBox(x, y, wert)):
        return 1
    return 0


def checkVertikal(x, wert):
    for i in xrange(9):
        if(pitch[i][x] == wert):
            #logging.debug("nein V " + str(wert))
            return 1
    #print("ja V ", wert)
    return 0


def checkHorizontal(y, wert):
    for i in xrange(9):
        if(pitch[y][i] == wert):
            #print("nein H", wert)
            return 1
    #print("ja H ", wert)
    return 0


def checkBox(x, y, wert):
    xBox = (int)(x / 3) * 3
    yBox = (int)(y / 3) * 3
    #print("checkBox x: ", x, y, xBox,yBox)
    #print("Wert: ", wert)
    for i in xrange(yBox, yBox+3):
        for j in xrange(xBox, xBox+3):
            if(pitch[i][j] == wert):
                #print("nein B ", wert, xBox, yBox)
                return 1
    #print("ja B ", wert, xBox, yBox)
    return 0


def solve(x, y):
    if(x == 9):
        y += 1 
        x = 0
        if(y == 9):
            return 1
    if(pitch[y][x] > 0):
        return solve(x+1, y)
    for i in xrange(9+1):
        if(not(check(x, y, i))):
            pitch[y][x] = i
            #logging.debug(printPitch())           # nice debug
            if(solve(x+1, y)):
                global solution
                solution += 1
                print("Loesung ", solution, "\n")
                printPitch()
    pitch[y][x] = 0
    return 0


def usage():
    print("usage ./sudoku.py name_der_sudoku_datei.txt")


def printPitch():
    for i in xrange(9):
        print("\n\t", end="")
        for j in xrange(9):
            print(pitch[i][j], " ", end='')
    print("\n") 


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


    except IOError:
        logging.debug("file " + filename + "does not exitst")


if __name__ == "__main__":
    solution = 0
    pitch = [[],[],[],[],[],[],[],[],[]]
    n = len(sys.argv)
    if n == 1 or n > 2:
        usage()
        exit()
    else:
        slurpFileToPitch(sys.argv[1])

    printPitch()
    solve(0, 0)

