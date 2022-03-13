import threading
import time

counter = 0
blokada = threading.Lock()


class Licznik(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        print(f"Startuje wątek {self.name}")
        blokada.acquire()
        countDown(self.name, self.delay)
        blokada.release()
        print(f"Kończę wątek {self.name}")


def countDown(name, delay):
    global counter
    counter = 5

    while counter:
        time.sleep(delay)
        print(f"Wątek {name} odliczanie: {counter}")
        counter -= 1


t1 = Licznik('A', 0.5)
t2 = Licznik('B', 0.75)

t1.start()
t2.start()

t1.join()
t2.join()

print("Koniec")
