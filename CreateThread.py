import threading

counter = 0
def Mythread1():
    global counter
    for i in range(100000):
        counter += 1
def Mythread2():
    global counter
    for i in range(100000):
        counter += -1

if __name__ == '__main__':
    thread1 = threading.Thread(target = Mythread1)
    thread2 = threading.Thread(target = Mythread2)
    thread1.start() #start thread1
    thread2.start() #start thread2
    thread1.join() #wait for thread1 to finish
    thread2.join() #wait for thread2 to finish
    print("counter: ", counter)