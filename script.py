#!/usr/bin/python

import sys,random,os
from os import listdir
from os.path import isfile, join
#constants
MAX_EXERCISES = 30
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
        exer = exer + 'ex'+repr(i+1) + ' '
    f.write('(define (problem file{!r})(:domain domini)\n'
            '(:objects\n'
            '   dia1 dia2 dia3 dia4 dia5 dia6 dia7 dia8 dia9 dia10 dia11 dia12 dia13 dia14 dia15 - dia\n'
            '   d1 d2 d3 d4 d5 d6 d7 d8 d9 d10 - dificultat\n'
            '   {} - exercici\n'
            '   c0 c1 c2 c3 c4 c5 c6 - cardinalitat\n'
            ')\n'.format(versionfile,exer)
    )
    f.write(
          '(:init\n'
          '\t(es_dia_posterior dia2 dia1)\n'
          '\t(es_dia_posterior dia3 dia2)\n'
          '\t(es_dia_posterior dia4 dia3)\n'
          '\t(es_dia_posterior dia5 dia4)\n'
          '\t(es_dia_posterior dia6 dia5)\n'
          '\t(es_dia_posterior dia7 dia6)\n'
          '\t(es_dia_posterior dia8 dia7)\n'
          '\t(es_dia_posterior dia9 dia8)\n'
          '\t(es_dia_posterior dia10 dia9)\n'
          '\t(es_dia_posterior dia11 dia10)\n'
          '\t(es_dia_posterior dia12 dia11)\n'
          '\t(es_dia_posterior dia13 dia12)\n'
          '\t(es_dia_posterior dia14 dia13)\n'
          '\t(es_dia_posterior dia15 dia14)\n'
          '\t(es_dificultat_posterior d2 d1)\n'
          '\t(es_dificultat_posterior d3 d2)\n'
          '\t(es_dificultat_posterior d4 d3)\n'
          '\t(es_dificultat_posterior d5 d4)\n'
          '\t(es_dificultat_posterior d6 d5)\n'
          '\t(es_dificultat_posterior d7 d6)\n'
          '\t(es_dificultat_posterior d8 d7)\n'
          '\t(es_dificultat_posterior d9 d8)\n'
          '\t(es_dificultat_posterior d10 d9)\n'

          '\t(es_card_posterior c1 c0)\n'
          '\t(es_card_posterior c2 c1)\n'
          '\t(es_card_posterior c3 c2)\n'
          '\t(es_card_posterior c4 c3)\n'
          '\t(es_card_posterior c5 c4)\n'
          '\t(es_card_posterior c6 c5)\n'

          '\t(cardinalitat_dia dia1 c0)\n'
          '\t(cardinalitat_dia dia2 c0)\n'
          '\t(cardinalitat_dia dia3 c0)\n'
          '\t(cardinalitat_dia dia4 c0)\n'
          '\t(cardinalitat_dia dia5 c0)\n'
          '\t(cardinalitat_dia dia6 c0)\n'
          '\t(cardinalitat_dia dia7 c0)\n'
          '\t(cardinalitat_dia dia8 c0)\n'
          '\t(cardinalitat_dia dia9 c0)\n'
          '\t(cardinalitat_dia dia10 c0)\n'
          '\t(cardinalitat_dia dia11 c0)\n'
          '\t(cardinalitat_dia dia12 c0)\n'
          '\t(cardinalitat_dia dia13 c0)\n'
          '\t(cardinalitat_dia dia14 c0)\n'
          '\t(cardinalitat_dia dia15 c0)\n'
          '\t(dia_actual dia1)\n'
    )
    for i,x in enumerate(iniDif):
        f.write('\t(dificultat_actual ex' + repr(i+1) + ' d'+repr(x) + ')\n')
    for (x,y) in precursors:
        f.write('\t(precursor ex'+repr(x)+ ' ex' + repr(y) + ')\n')
    for (x,y) in preparadors:
        f.write('\t(preparador ex'+repr(x)+ ' ex' + repr(y) + ')\n')
    f.write('\t) \n')
    f.write('(:goal (and (dia_actual dia15)\n')

    for (x,y) in goalDif:
        f.write('\t(dificultat_actual ex' + repr(x) + ' d'+repr(y) + ')\n')
    f.write('\t)\n)\n)')

def writeProblemExt4(numberEx,iniDif,goalDif,tempsIni,precursors,preparadors,versionfile):
    f = open('JocsDeProva/Ext4/file'+repr(versionfile)+'.pddl','w')
    exer = ''
    for i in range(numberEx):
        exer = exer + 'ex'+repr(i+1) + ' '
    f.write('(define (problem file{!r})(:domain domini)\n'
            '(:objects\n'
            '   dia1 dia2 dia3 dia4 dia5 dia6 dia7 dia8 dia9 dia10 dia11 dia12 dia13 dia14 dia15 - dia\n'
            '   d1 d2 d3 d4 d5 d6 d7 d8 d9 d10 - dificultat\n'
            '   {} - exercici\n'
            ')\n'.format(versionfile,exer)
    )
    f.write(
          '(:init\n'
          '\t(es_dia_posterior dia2 dia1)\n'
          '\t(es_dia_posterior dia3 dia2)\n'
          '\t(es_dia_posterior dia4 dia3)\n'
          '\t(es_dia_posterior dia5 dia4)\n'
          '\t(es_dia_posterior dia6 dia5)\n'
          '\t(es_dia_posterior dia7 dia6)\n'
          '\t(es_dia_posterior dia8 dia7)\n'
          '\t(es_dia_posterior dia9 dia8)\n'
          '\t(es_dia_posterior dia10 dia9)\n'
          '\t(es_dia_posterior dia11 dia10)\n'
          '\t(es_dia_posterior dia12 dia11)\n'
          '\t(es_dia_posterior dia13 dia12)\n'
          '\t(es_dia_posterior dia14 dia13)\n'
          '\t(es_dia_posterior dia15 dia14)\n'
          '\t(es_dificultat_posterior d2 d1)\n'
          '\t(es_dificultat_posterior d3 d2)\n'
          '\t(es_dificultat_posterior d4 d3)\n'
          '\t(es_dificultat_posterior d5 d4)\n'
          '\t(es_dificultat_posterior d6 d5)\n'
          '\t(es_dificultat_posterior d7 d6)\n'
          '\t(es_dificultat_posterior d8 d7)\n'
          '\t(es_dificultat_posterior d9 d8)\n'
          '\t(es_dificultat_posterior d10 d9)\n'
          '\t(dia_actual dia1)\n'
    )
    #(=(tempsEx ex1) 10)
    for i,x in enumerate(tempsIni):
        f.write('\t(=(tempsEx ex' + repr(i + 1) + ') ' + repr(x) +')\n')
    for i,x in enumerate(iniDif):
        f.write('\t(dificultat_actual ex' + repr(i+1) + ' d'+repr(x) + ')\n')
    for (x,y) in precursors:
        f.write('\t(precursor ex'+repr(x)+ ' ex' + repr(y) + ')\n')
    for (x,y) in preparadors:
        f.write('\t(preparador ex'+repr(x)+ ' ex' + repr(y) + ')\n')
    f.write('\t) \n')
    f.write('(:goal (and (dia_actual dia15)\n')

    for (x,y) in goalDif:
        f.write('\t(dificultat_actual ex' + repr(x) + ' d'+repr(y) + ')\n')
    f.write('\t)\n)\n)')


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
            iniDif = list(map(lambda x: random.randint(1,10),range(1,numberEx+1)))
            goalDif = list(map(lambda x: (x,random.randint(iniDif[x-1],10)),goalDif))
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
            iniDif = list(map(lambda x: random.randint(1,10),range(1,numberEx+1)))
            goalDif = list(map(lambda x: (x,random.randint(iniDif[x-1],10)),goalDif))
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
