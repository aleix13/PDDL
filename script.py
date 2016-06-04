#!/usr/bin/python

import sys,random

def ChooseStringOptions(inp,errorMessage,*options):
    while(True):
        i = 0
        for x in options:
            if inp == x:
                return i
            i+=1
        else:
            inp = input(errorMessage)

def checkType(attr,type,pred=lambda x: True,errorMessage1='',errorMessage2 = ''):
    while(True):
        try:
            attr = type(attr)
            while not pred(attr):
                attr=input(errorMessage2)
                attr = type(attr)
            break
        except:
            attr=input(errorMessage1)
    return attr

def randomGenerate(versionfile):
    random.seed()
    numberFiles = input('How many files do you want to generate? ')
    numberFiles = checkType(numberFiles,lambda x: int(x),lambda x: x >= 0,
    'this is not a number,try again, how many files do you want to generate? ',
    'this is not a positive number,try again, how many files do you want to generate? ')
    msg = 'Which extension do you want to use, extension3 or extension4 (3/4)? '
    ext = input(msg)
    ext = ChooseStringOptions(ext,'Try again, ' + msg,'3','4')
    if ext: #extension3
        #do something
    else:   #extension4
        #do something



#-----MAIN-----
while(True):
    try:
        versionfile = open('.actual_version', 'r')
        v = int(versionfile.readline())
        break
    except:
        versionfile = open('.actual_version','w')
        versionfile.write("0\n")

is_random = input('Generate Random or Interactively? (R/I): ')
is_random = ChooseStringOptions(is_random,'Try again,generate Random or Interactively? (I/R): ','I','R')
if is_random:
    randomGenerate(versionfile)

else:
    interactiveGenerate()
