#!/usr/bin/python3
import pickle
global EventDict
def main():
    global EventDict
    EventLoader()

def EventLoader():
    global EventDict
    with open('SchoolEvents.save', 'rb') as EventLoad:
        while True:
            try:
                EventDict = pickle.load(EventLoad)
            except EOFError:
                break
                
if __name__ == '__main__':
    main()