from multiprocessing import *

def manyGreetings2():
    name = raw_input("Enter your name: ")
    numProc = input("How many processes? ")

    for i in range(numProc):
        (Process(target=sayHi2, args=(name,))).start()