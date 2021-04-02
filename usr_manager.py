#! /usr/bin/python3
import pickle
global usrDict
def main():
    global usrDict
    usrLoader()
    #print(usrDict)

def usrLoader():
    global usrDict
    with open('usr.save', 'rb') as usrLoad:
        while True:
            try:
                usrDict = pickle.load(usrLoad)
            except EOFError:
                break
def usrSaver():
    global usrDict
    with open('usr.save', 'wb') as usrSave:
        pickle.dump(usrDict, usrSave)

def usrAdd(usr, classroom):
    global usrDict
    usrLoader()
    if Whereis(usr) == 0:
        usrDict[str(classroom)].append(usr)
        usrSaver()
    else:
        usrChange(usr, classroom)

def usrChange(usr, after):
    global usrDict
    usrLoader()
    usrClass = str(Whereis(usr))
    usrIndex = usrDict[usrClass].index(usr)
    del usrDict[usrClass][usrIndex]
    usrSaver()
    usrAdd(usr, after)

def Whereis(usr):
    global usrDict
    usrLoader()
    for i in range(101, 113):
        if usr in usrDict[str(i)]:
            return i
        else:
            noInOne = True
    for i in range(201, 213):
        if usr in usrDict[str(i)]:
            return i
        else:
            noInTwo = True
    for i in range(301, 314):
        if usr in usrDict[str(i)]:
            return i
        else:
            noInThree = True
    if noInOne and noInTwo and noInThree:
        return 0

if __name__ == '__main__':
    main()