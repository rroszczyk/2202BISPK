from math import sqrt
import queue
import threading
import time

kolejka = queue.Queue()

def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return x
    if x % 2 == 0:
        return False
    limit = int(sqrt(x)) + 1
    for i in range(3, limit, 2):
        if x % i == 0:
            return False
    return x

def processQueue():
    while True:
        try:
            x = kolejka.get(block = False)
        except queue.Empty:
            return
        else:
            print(f"Liczba {x} jest liczbą pierwszą: {is_prime(x)}")
        time.sleep(1)

class Zadanie(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print(f"Startuje zadanie {self.name}")
        processQueue()
        print(f"Kończę zadanie {self.name}")


for i in range(1000, 1100):
    kolejka.put(i)

t1 = Zadanie("A")
t2 = Zadanie("B")
t3 = Zadanie("C")

t1.start()
t2.start()
t3.start()

time.sleep(10)
for i in range(2000, 2050):
    kolejka.put(i)

t1.join()
t2.join()
t3.join()

