import datetime
import pickle
global TimesDict

def main():
    global TimesDict
    TimeLoader()
    #print(TimesDict)

def TimeSaver():
    global TimesDict
    with open('time.dat', 'wb') as TimeSave:
        pickle.dump(TimesDict, TimeSave)

def TimeLoader():
    global TimesDict
    with open('time.dat', 'rb') as TimeLoad:
        TimesDict = pickle.load(TimeLoad)
#opt=0: start   // opt=1: stop and return second+microsecond
def Benchmark(opt, command):
    global TimesDict
    TimeLoader()
    if opt == 0:
        now0 = datetime.datetime.now()
    if opt == 1:
        now1 = datetime.datetime.now()
        fin_val = now1 - now0
        final_time = int(fin_val.seconds) + int(fin_val.microseconds) / 1000000
        TimesDict[str(command)].append(final_time)
        TimeSaver()

def Average(command):
    global TimesDict
    TimeLoader()
    time_sum = 0
    how_many = len(TimesDict[str(command)])
    for i in range(how_many):
        time_sum = time_sum + TimesDict[str(command)][i]
        #print(TimesDict[str(command)][i], how_many, i)
    try:
        return time_sum / how_many
    except ZeroDivisionError:
        return 'No data'

if __name__ == '__main__':
    main()
else:
    TimeLoader()