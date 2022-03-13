from math import sqrt
import threading
import time

# zmodyfikować program aby korzystał z poniższych struktur danych zamiast kolejki
lista = []
currentElement = 0
blokada = threading.Lock()

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
    global lista
    global currentElement

    while True:
        with blokada:
            if (currentElement > len(lista)):
                return
            x = lista[currentElement]
            currentElement += 1
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
    lista.append(i)

t1 = Zadanie("A")
t2 = Zadanie("B")
t3 = Zadanie("C")

t1.start()
t2.start()
t3.start()

time.sleep(10)
with blokada:
    for i in range(2000, 2050):
        lista.append(i)

t1.join()
t2.join()
t3.join()

