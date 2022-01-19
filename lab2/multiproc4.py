from multiprocessing import *

# def sayHi3(personName):
#     print("Hi", personName, "from process", current_process().name, "- pid", current_process().pid)

# def manyGreetings3():
#     print("Hi from process", current_process().pid, "(parent process)")

#     personName = "Jimmy"
#     for i in range(10):
#         Process(target=sayHi3, args=(personName,), name=str(i)).start()

# manyGreetings3()


# ----------------------------------------------------------------


# def sayHi4(lock, name):
#     lock.acquire()
#     print("Hi", name, "from process", current_process().pid)
#     lock.release()

# def manyGreetings4():
#     lock1 = Lock()

#     print("Hi from process", current_process().pid, "(main process)")

#     for i in range(10):
#         Process(target=sayHi4, args=(lock1, "p"+str(i))).start()

# manyGreetings4()


# ----------------------------------------------------------------



def sayHi5(lock, name):
    lock.acquire()
    print("Hiddy-ho!\tI'm worker", name, "and today I have to dig hole", current_process().pid)
    lock.release()

def manyGreetings5():
    lock1 = Lock()
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    print("Hi from process", current_process().pid, "(main process)")
    n = int(input("Enter number of workers: "))
    for i in range(n):
        Process(target=sayHi5, args=(lock1, "worker "+alpha[i])).start()

manyGreetings5()