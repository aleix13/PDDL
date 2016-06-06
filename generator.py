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
            if inp.lower() == x.lower():
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

def writeProblemExt3(numberEx,iniDif,goalDif,precursors,preparadors,versionfile=-1,name=''):
    if(name == ''):
        f = open('JocsDeProva/Ext3/file'+repr(versionfile)+'.pddl','w')
    else:
        f = open(name + '.pddl','w')
    exer = ''
    for i in range(numberEx):
        exer = exer + 'ex'+repr(i+1) + ' '
    #header of the file
    f.write('(define (problem file{!r})(:domain domini)\n'
            '(:objects\n'
            '   dia1 dia2 dia3 dia4 dia5 dia6 dia7 dia8 dia9 dia10 dia11 dia12 dia13 dia14 dia15 - dia\n'
            '   d1 d2 d3 d4 d5 d6 d7 d8 d9 d10 - dificultat\n'
            '   {} - exercici\n'
            '   c0 c1 c2 c3 c4 c5 c6 - cardinalitat\n'
            ')\n'.format(versionfile,exer)
    )
    #some inits
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
    #initial dificulties
    for i,x in enumerate(iniDif):
        f.write('\t(dificultat_actual ex' + repr(i+1) + ' d'+repr(x) + ')\n')
    #precursors
    for (x,y) in precursors:
        f.write('\t(precursor ex'+repr(x)+ ' ex' + repr(y) + ')\n')
    #preparadors
    for (x,y) in preparadors:
        f.write('\t(preparador ex'+repr(x)+ ' ex' + repr(y) + ')\n')

    f.write('\t) \n')
    f.write('(:goal (and (dia_actual dia15)\n')

    #goal dificulties
    for (x,y) in goalDif:
        f.write('\t(dificultat_actual ex' + repr(x) + ' d'+repr(y) + ')\n')
    f.write('\t)\n)\n)')

def writeProblemExt4(numberEx,iniDif,goalDif,tempsIni,precursors,preparadors,versionfile=-1,name=''):
    if(name == ''):
        f = open('JocsDeProva/Ext4/file'+repr(versionfile)+'.pddl','w')
    else:
        f = open(name + '.pddl','w')
    exer = ''
    for i in range(numberEx):
        exer = exer + 'ex'+repr(i+1) + ' '
    #file header
    f.write('(define (problem file{!r})(:domain domini)\n'
            '(:objects\n'
            '   dia1 dia2 dia3 dia4 dia5 dia6 dia7 dia8 dia9 dia10 dia11 dia12 dia13 dia14 dia15 - dia\n'
            '   d1 d2 d3 d4 d5 d6 d7 d8 d9 d10 - dificultat\n'
            '   {} - exercici\n'
            ')\n'.format(versionfile,exer)
    )
    #some init declarations
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
          '\t(=(tempsTotal) 0)\n'
    )
    #time for each exercice
    for i,x in enumerate(tempsIni):
        f.write('\t(=(tempsEx ex' + repr(i + 1) + ') ' + repr(x) +')\n')
    #initial difficulty
    for i,x in enumerate(iniDif):
        f.write('\t(dificultat_actual ex' + repr(i+1) + ' d'+repr(x) + ')\n')
    #precursors
    for (x,y) in precursors:
        f.write('\t(precursor ex'+repr(x)+ ' ex' + repr(y) + ')\n')
    #preparators
    for (x,y) in preparadors:
        f.write('\t(preparador ex'+repr(x)+ ' ex' + repr(y) + ')\n')

    f.write('\t) \n')
    f.write('(:goal (and (dia_actual dia15)\n')

    #goal difficulties
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

    if ext: #---------------------------------extension3---------------------------------
        for n in range(numberFiles):
            numberEx = random.randint(1,MAX_EXERCISES)
            numGoalEx = random.randint(1,numberEx)
            goalDif = random.sample(range(1,numberEx+1),numGoalEx)                                  #a sample from original excercices
            iniDif = list(map(lambda x: random.randint(1,10),range(1,numberEx+1)))                  #initial dificulties from 1 to 10_
            goalDif = list(map(lambda x: (x,random.randint(iniDif[x-1],10)),goalDif))               #each member of a sample is assigned random objective >= initial difficulty

            #Each ocurrences{i} contents a set of element that can be precursors or preparators for exercice i
            ocurrences = {}
            for x in range(1,numberEx+1):
                oc = set(range(1,numberEx+1))
                oc.remove(x)
                ocurrences[x] = oc

            activities = [0 for x in range(numberEx)]                                               #this stores the number of activities for each exercice

            numPrecursor = numberEx - random.randint(int(numberEx*(1-MAX_RATIO_PREC)),numberEx)
            numPreparador = numberEx - random.randint(int(numberEx*(1-MAX_RATIO_PREP)),numberEx)
            precursors = []
            preparadors = []
            maxIter = random.randint(5,100)*numPrecursor

            #---------------------------------calculate precursors---------------------------------
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

            #---------------------------------calculate preparators--------------------------------
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


            #write the problem into a file
            writeProblemExt3(numberEx,iniDif,goalDif,precursors,preparadors,versionfile=v3)
            v3+=1

    else:       #---------------------------------extension4---------------------------------
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

            #---------------------------------calculate precursors---------------------------------
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

            #---------------------------------calculate preparators---------------------------------
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


            writeProblemExt4(numberEx,iniDif,goalDif,tempsIni,precursors,preparadors,versionfile=v4)
            v4+=1


def interactiveGenerate():
    msg = 'Which extension do you want to use, extension3 or extension4 (3/4)? '
    ext = input(msg)
    ext = ChooseStringOptions(ext,'Try again, ' + msg,'4','3')

    if ext:     #---------------------------------extension3---------------------------------
        msg = 'How many exercices do you want to do? (> 0): '
        numberEx = input(msg)
        numberEx = checkType(numberEx,lambda x: int(x), lambda x: x > 0, msg,msg)


        #---------------------------------initial difficulty---------------------------------
        msg = 'Do you want to enter each initial difficulty or assign it randomly? (E/R): '
        enter = input(msg)
        enter = ChooseStringOptions(enter,msg,'R','E')
        print(enter)
        iniDif = []
        if enter:
            msg = 'Enter each exercise initial difficulty one at a time: (1 - 10)'
            print(msg)
            for i in range(numberEx):
                msg = 'ex' + repr(i+1) + ' initial difficulty: (1 - 10)'
                dif = input(msg)
                dif = checkType(dif,lambda x: int(x),lambda x: x >= 1 and x <= 10,msg,msg)
                iniDif.append(dif)
        else:
            iniDif = list(map(lambda x: random.randint(1,10),range(1,numberEx+1)))

        #---------------------------------goal difficulty---------------------------------
        goalDif = []
        visited = [False for x in range(numberEx)]
        msg = 'Do you want to enter each final difficulty or assign it randomly? (E/R)'
        enter = input(msg)
        enter = ChooseStringOptions(enter,msg,'R','E')
        if enter:
            msg = 'Enter each final difficulty one at a time, When finnished enter -1'
            print(msg)
            num = 0
            while(True):
                num+=1
                msg = 'enter exercicie number '
                ex = input(msg)
                ex = checkType(ex,lambda x: int(x),lambda x: x >= -1 and x != 0 and not visited[x-1] and x <= numberEx,msg,msg)
                visited[ex - 1] = True
                if ex != -1:
                    msg = 'enter difficulty (1 - 10): '
                    dif = input(msg)
                    dif = checkType(dif,lambda x: int(x),lambda x: x >= 1 and x <= 10,'Try again: '+msg,'Try again: ' +msg)
                    if(num == numberEx):
                        break
                    goalDif.append((ex,dif))
                else:
                    break
        else:
            msg = 'Enter number of exercices that will have final difficulty: '
            numGoalEx = input(msg)
            numGoalEx = checkType(numGoalEx,lambda x: int(x), lambda x: x >= 0 and x <= numberEx,msg,'must be less or equal than the total number of exercices, '+msg)
            goalDif = random.sample(range(1,numberEx+1),numGoalEx)
            goalDif = list(map(lambda x: (x,random.randint(iniDif[x-1],10)),goalDif))

        #---------------------------------calculate precursors---------------------------------
        precursors = []
        visited = [False for x in range(numberEx)]
        msg = 'Enter each precursor and then its exercicie, When finnished enter -1'
        print(msg)
        while(True):
            msg = 'enter precursor number '
            pr = input(msg)
            pr = checkType(pr,lambda x: int(x),lambda x: x >= -1 and x != 0 and x<= numberEx,msg,msg)
            if pr != -1:
                msg = 'enter exercicie: '
                ex = input(msg)
                ex = checkType(ex,lambda x: int(x),lambda x: x >= 1 and not visited[x-1] and x != pr and x <= numberEx,msg,'Must exist and not be visited and be different than predecesor\n'+msg)
                precursors.append((pr,ex))
                visited[ex - 1] = True
            else:
                break

        #---------------------------------calculate preparator---------------------------------
        preparadors = []
        msg = 'Enter each preparator and then its exercicie, When finnished enter -1'
        print(msg)
        while(True):
            msg = 'enter preparator number '
            pr = input(msg)
            pr = checkType(pr,lambda x: int(x),lambda x: x >= -1 and x!=0 and x <= numberEx,msg,msg)
            if pr != -1:
                msg = 'enter exercicie: '
                ex = input(msg)
                ex = checkType(ex,lambda x: int(x),lambda x: x >= 1 and x != pr,msg,'Must exist and be different than preparator\n'+msg)
                preparadors.append((pr,ex))
            else:
                break


        fileName = input('Enter the name of the file that will be saved (auto extension): ')
        writeProblemExt3(numberEx,iniDif,goalDif,precursors,preparadors,name=fileName)


    else:       #---------------------------------extension4---------------------------------
        msg = 'How many exercices do you want to do? (> 0): '
        numberEx = input(msg)
        numberEx = checkType(numberEx,lambda x: int(x), lambda x: x > 0, msg,msg)

        #---------------------------------initial difficulties---------------------------------
        msg = 'Do you want to enter each initial difficulty or assign it randomly? (E/R): '
        enter = input(msg)
        enter = ChooseStringOptions(enter,msg,'R','E')
        print(enter)
        iniDif = []
        if enter:
            msg = 'Enter each exercise initial difficulty one at a time: (0 - 10)'
            print(msg)
            for i in range(numberEx):
                msg = 'ex' + repr(i+1) + ' initial difficulty: (1 - 10)'
                dif = input(msg)
                dif = checkType(dif,lambda x: int(x),lambda x: x >= 1 and x <= 10,msg,msg)
                iniDif.append(dif)
        else:
            iniDif = list(map(lambda x: random.randint(1,10),range(1,numberEx+1)))

        #---------------------------------goal difficulties---------------------------------
        goalDif = []
        visited = [False for x in range(numberEx)]
        msg = 'Do you want to enter each final difficulty or assign it randomly? (E/R)'
        enter = input(msg)
        enter = ChooseStringOptions(enter,msg,'R','E')
        if enter:
            msg = 'Enter each final difficulty one at a time, When finnished enter -1'
            print(msg)
            num = 0
            while(True):
                num+=1
                msg = 'enter exercicie number '
                ex = input(msg)
                ex = checkType(ex,lambda x: int(x),lambda x: x >= -1 and x != 0 and not visited[x-1] and x <= numberEx,msg,msg)
                visited[ex - 1] = True
                if ex != -1:
                    msg = 'enter difficulty (1 - 10): '
                    dif = input(msg)
                    dif = checkType(dif,lambda x: int(x),lambda x: x >= 1 and x <= 10 and x<= numberEx,'Try again: '+msg,'Try again: ' +msg)
                    if(num == numberEx):
                        break
                    goalDif.append((ex,dif))
                else:
                    break
        else:
            msg = 'Enter number of exercices that will have final difficulty: '
            numGoalEx = input(msg)
            numGoalEx = checkType(numGoalEx,lambda x: int(x), lambda x: x >= 0 and x <= numberEx,msg,'must be less or equal than the total number of exercices, '+msg)
            goalDif = random.sample(range(1,numberEx+1),numGoalEx)
            goalDif = list(map(lambda x: (x,random.randint(iniDif[x-1],10)),goalDif))

        #---------------------------------exercice time---------------------------------
        msg = 'Do you want to enter each time for exercise or assign it randomly? (E/R): '
        enter = input(msg)
        enter = ChooseStringOptions(enter,msg,'R','E')
        print(enter)
        tempsIni = []
        if enter:
            msg = 'Enter each exercise time one at a time: (1 - 90)'
            print(msg)
            for i in range(numberEx):
                msg = 'ex' + repr(i+1) + ' time: (1 - 90)'
                dif = input(msg)
                dif = checkType(dif,lambda x: int(x),lambda x: x >= 1 and x <= 90,msg,msg)
                tempsIni.append(dif)
        else:
            tempsIni = list(map(lambda x: random.randint(1,10),range(1,numberEx+1)))

        #---------------------------------calculate precursors---------------------------------
        precursors = []
        visited = [False for x in range(numberEx)]
        msg = 'Enter each precursor and then its exercicie, When finnished enter -1'
        print(msg)
        while(True):
            msg = 'enter precursor number '
            pr = input(msg)
            pr = checkType(pr,lambda x: int(x),lambda x: x >= -1 and x != 0 and x <= numberEx ,msg,msg)
            if pr != -1:
                msg = 'enter exercicie: '
                ex = input(msg)
                ex = checkType(ex,lambda x: int(x),lambda x: x >= 1 and not visited[x-1] and x != pr and x <= numberEx,msg,'Must exist and not be visited and be different than predecesor\n'+msg)
                precursors.append((pr,ex))
                visited[ex - 1] = True
            else:
                break

        #---------------------------------calculate preparators---------------------------------
        preparadors = []
        msg = 'Enter each preparator and then its exercicie, When finnished enter -1'
        print(msg)
        while(True):
            msg = 'enter preparator number '
            pr = input(msg)
            pr = checkType(pr,lambda x: int(x),lambda x: x >= -1 and x!=0 and x <= numberEx,msg,msg)
            if pr != -1:
                msg = 'enter exercicie: '
                ex = input(msg)
                ex = checkType(ex,lambda x: int(x),lambda x: x >= 1 and x != pr and x <= numberEx,msg,'Must exist and be different than preparator\n'+msg)
                preparadors.append((pr,ex))
            else:
                break

        fileName = input('Enter the name of the file that will be saved (auto extension): ')
        writeProblemExt4(numberEx,iniDif,goalDif,tempsIni,precursors,preparadors,name=fileName)




##---------------------------------MAIN---------------------------------
pathExt3 = './JocsDeProva/Ext3/'
pathExt4 = './JocsDeProva/Ext4/'
#check if folders exists, if not, create them
if not os.path.exists(pathExt3):
    os.makedirs(pathExt3)
if not os.path.exists(pathExt4):
    os.makedirs(pathExt4)
filesExt3 = [f for f in listdir(pathExt3) if isfile(join(pathExt3, f))]
filesExt4 = [f for f in listdir(pathExt4) if isfile(join(pathExt4, f))]

v3 = v4 = 0
#check version number for extension3
for x in filesExt3:
    if(x[0:4] == 'file'):
        num = x[4:(5+(len(x) - 10))]
        try:
            num = int(num)
        except:
            pass
        if isinstance(num,int):
            if(num > v3):
                v3 = num
#check version number for extension4
for x in filesExt4:
    if(x[0:4] == 'file'):
        num = x[4:(5+(len(x) - 10))]
        try:
            num = int(num)
        except:
            pass
        if isinstance(num,int):
            if(num > v4):
                v4 = num

is_random = input('Generate Random or Interactively? (R/I): ')
is_random = ChooseStringOptions(is_random,'Try again,generate Random or Interactively? (R/I): ','I','R')
if is_random:
    #generate randomly each file
    randomGenerate(v3+1,v4+1)

else:
    #generate Interactively each file
    interactiveGenerate()
