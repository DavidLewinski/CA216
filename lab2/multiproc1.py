from multiprocessing import *

def sayHi1():
    print("Hi from process", current_process().pid, "(child 1)")

def sayHi2():
    print("Hi from process", current_process().pid, "(child 2)")

def procEx():
    print("Hi from process", current_process().pid, "(parent process)")

    otherProc = Process(target=sayHi1, args=())
    otherProc2 = Process(target=sayHi2, args=())

    otherProc.start()
    otherProc2.start()

### execute
procEx()