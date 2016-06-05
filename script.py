#!/usr/bin/python

import sys,random,os
from os import listdir
from os.path import isfile, join
#constants
MAX_EXERCISES = 60
MAX_RATIO_PREC = 0.15
MAX_RATIO_PREP = 0.5


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

def writeProblemExt3(numberEx,iniDif,goalDif,precursors,preparadors,versionfile):
    f = open('JocsDeProva/Ext3/file'+repr(versionfile)+'.pddl','w')
    exer = ''
    for i in range(numberEx):
        exer = exer + 'ex'+repr(i) + ' '
    f.write('(define (problem file{!r})(:domain domini)\n'
            '(:objects\n'
            '   dia1 dia2 dia3 dia4 dia5 dia6 dia7 dia8 dia9 dia10 dia11 dia12 dia13 dia14 dia15 - dia\n'
            '   d1 d2 d3 d4 d5 d6 d7 d8 d9 d10 - dificultat\n'
            '   {} - exercici\n'
            '   c0 c1 c2 c3 c4 c5 c6 - cardinalitat\n'
            ')\n'.format(versionfile,exer)
    )

def writeProblemExt4(numberEx,iniDif,goalDif,tempsIni,precursors,preparadors,versionfile):
    f = open('JocsDeProva/Ext4/file'+versionfile+'.pddl','w')
def randomGenerate(v3,v4):
    random.seed()
    numberFiles = input('How many files do you want to generate? ')
    numberFiles = checkType(numberFiles,lambda x: int(x),lambda x: x >= 0,
    'this is not a number,try again, how many files do you want to generate? ',
    'this is not a positive number,try again, how many files do you want to generate? ')
    msg = 'Which extension do you want to use, extension3 or extension4 (3/4)? '
    ext = input(msg)
    ext = ChooseStringOptions(ext,'Try again, ' + msg,'4','3')
    if ext: #extension3
        for n in range(numberFiles):
            numberEx = random.randint(1,MAX_EXERCISES)
            numGoalEx = random.randint(1,numberEx)
            goalDif = random.sample(range(1,numberEx+1),numGoalEx)
            goalDif = list(map(lambda x: (x,random.randint(1,10)),goalDif))
            iniDif = list(map(lambda x: random.randint(1,10),range(1,numberEx+1)))
            ocurrences = {}
            for x in range(1,numberEx+1):
                oc = set(range(1,numberEx+1))
                oc.remove(x)
                ocurrences[x] = oc
            activities = [0 for x in range(numberEx)]
            numPrecursor = numberEx - random.randint(int(numberEx*(1-MAX_RATIO_PREC)),numberEx)
            numPreparador = numberEx - random.randint(int(numberEx*(1-MAX_RATIO_PREP)),numberEx)
            precursors = []
            preparadors = []
            maxIter = random.randint(5,100)*numPrecursor
            while(ocurrences and numPrecursor > 0 and maxIter > 0):
                maxIter -= 1
                x = random.choice(list(ocurrences.keys()))
                if(activities[x-1] < 1):
                    if(not ocurrences[x]):
                        break
                    prec = random.choice(list(ocurrences[x]))
                    ocurrences[x].remove(prec)
                    ocurrences[prec].remove(x)
                    if(not ocurrences[x]):
                        del ocurrences[x]
                    if(not ocurrences[prec]):
                        del ocurrences[prec]
                    numPrecursor -= 1
                    precursors.append((prec,x))
                    activities[x-1] += 1

            maxIter = random.randint(5,100)*numPreparador
            while(ocurrences and numPreparador > 0 and maxIter > 0):
                maxIter -= 1
                x = random.choice(list(ocurrences.keys()))
                if(activities[x-1] < 6):
                    if(not ocurrences[x]):
                        break
                    prec = random.choice(list(ocurrences[x]))
                    ocurrences[x].remove(prec)
                    ocurrences[prec].remove(x)
                    if(not ocurrences[x]):
                        del ocurrences[x]
                    if(not ocurrences[prec]):
                        del ocurrences[prec]
                    numPreparador -= 1
                    preparadors.append((prec,x))
                    activities[x-1] += 1
            writeProblemExt3(numberEx,iniDif,goalDif,precursors,preparadors,v3)
            v3+=1

    else:       #extension4
        for n in range(numberFiles):
            numberEx = random.randint(1,MAX_EXERCISES)
            numGoalEx = random.randint(1,numberEx)
            goalDif = random.sample(range(1,numberEx+1),numGoalEx)
            goalDif = list(map(lambda x: (x,random.randint(1,10)),goalDif))
            iniDif = list(map(lambda x: random.randint(1,10),range(1,numberEx+1)))
            ocurrences = {}
            for x in range(1,numberEx+1):
                oc = set(range(1,numberEx+1))
                oc.remove(x)
                ocurrences[x] = oc
            visited = [False for i in range(numberEx)]
            temps = [random.randint(1,90) for i in range(numberEx)]
            tempsIni = list(temps)
            numPrecursor = numberEx - random.randint(int(numberEx*(1-MAX_RATIO_PREC)),numberEx)
            numPreparador = numberEx - random.randint(int(numberEx*(1-MAX_RATIO_PREP)),numberEx)
            precursors = []
            preparadors = []
            maxIter = random.randint(5,100)*numPrecursor
            while(ocurrences and numPrecursor > 0 and maxIter > 0):
                maxIter -= 1
                x = random.choice(list(ocurrences.keys()))
                if(not ocurrences[x]):
                    break
                prec = random.choice(list(ocurrences[x]))
                if(temps[x-1] + temps[prec - 1] <= 90 and not visited[x-1]):
                    ocurrences[x].remove(prec)
                    ocurrences[prec].remove(x)
                    if(not ocurrences[x]):
                        del ocurrences[x]
                    if(not ocurrences[prec]):
                        del ocurrences[prec]
                    numPrecursor -= 1
                    precursors.append((prec,x))
                    visited[x-1] = True
                    temps[x-1] += temps[prec - 1]

            maxIter = random.randint(5,100)*numPreparador
            while(ocurrences and numPreparador > 0 and maxIter > 0):
                maxIter -= 1
                x = random.choice(list(ocurrences.keys()))
                if(not ocurrences[x]):
                    break
                prec = random.choice(list(ocurrences[x]))
                if(temps[x-1] + temps[prec - 1] <= 90):
                    ocurrences[x].remove(prec)
                    ocurrences[prec].remove(x)
                    if(not ocurrences[x]):
                        del ocurrences[x]
                    if(not ocurrences[prec]):
                        del ocurrences[prec]
                    numPreparador -= 1
                    preparadors.append((prec,x))
                    temps[x-1] += temps[prec - 1]

            writeProblemExt4(numberEx,iniDif,goalDif,tempsIni,precursors,preparadors,v4)
            v4+=1








#-----MAIN-----
pathExt3 = './JocsDeProva/Ext3/'
pathExt4 = './JocsDeProva/Ext4/'
if not os.path.exists(pathExt3):
    os.makedirs(pathExt3)
if not os.path.exists(pathExt4):
    os.makedirs(pathExt4)
filesExt3 = [f for f in listdir(pathExt3) if isfile(join(pathExt3, f))]
filesExt4 = [f for f in listdir(pathExt4) if isfile(join(pathExt4, f))]

v3 = v4 = 0

for x in filesExt3:
    num = int(x[4:(5+(len(x) - 10))])
    if(num > v3):
        v3 = num

for x in filesExt4:
    num = int(x[4:(5+(len(x) - 10))])
    if(num > v4):
        v4 = num



is_random = input('Generate Random or Interactively? (R/I): ')
is_random = ChooseStringOptions(is_random,'Try again,generate Random or Interactively? (I/R): ','I','R')
if is_random:
    randomGenerate(v3+1,v4+1)

else:
    interactiveGenerate()
