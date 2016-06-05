#!/usr/bin/python

import sys,random

#constants
MAX_EXERCISES = 30


def ChooseStringOptions(inp,errorMessage,*options):
    while(True):
        for i,x in enumerate(options):
            if inp == x:
                return i
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
    ext = ChooseStringOptions(ext,'Try again, ' + msg,'4','3')
    if ext: #extension3
        numberEx = random.randint(1,MAX_EXERCISES)
        numGoalEx = random.randint(1,numberEx)
        goalDif = random.sample(range(1,numberEx+1),numGoalEx)
        goalDif = list(map(lambda x: (x,random.randint(1,10)),goalDif))
        iniDif = list(map(lambda x: random.randint(1,10),range(1,numberEx+1)))
        print(iniDif)




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
