from multiprocessing import *

def sayHi2(n):
    print("Hi", n, "from process", current_process().pid)


def manyGreetings():
    print("Hi from process", current_process().pid, "(main process)")

    name = input("Enter a name: ")
    n = int(input("Loop number of times: "))
    i = 0
    while i < n:
        p1 = Process(target=sayHi2, args=(name,))
        # p2 = Process(target=sayHi2, args=(name,))
        # p3 = Process(target=sayHi2, args=(name,))

        p1.start()
        # p2.start()
        # p3.start()
        i += 1

### execute
manyGreetings()