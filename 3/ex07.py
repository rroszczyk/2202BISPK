import threading
import time

blokadaA = threading.Lock()
blokadaB = threading.Lock()


def zadanieA():
    print("Startuję zadanie A")

    print("Oczekuję na blokadę A")
    blokadaA.acquire()
    print("Blokada A została założona, trwa obliczanie")
    time.sleep(2)

    print("Oczekuję na blokadę B")
    blokadaB.acquire()
    print("Blokada B została założona, trwa obliczanie")
    time.sleep(2)

    print("Wątek A zwalnia obie blokady")
    blokadaA.release()
    blokadaB.release()


def zadanieB():
    print("Startuję zadanie B")

    print("Oczekuję na blokadę B")
    blokadaB.acquire()
    print("Blokada B została założona, trwa obliczanie")
    time.sleep(2)

    print("Oczekuję na blokadę A")
    blokadaA.acquire()
    print("Blokada A została założona, trwa obliczanie")
    time.sleep(2)

    print("Wątek B zwalnia obie blokady")
    blokadaB.release()
    blokadaA.release()


t1 = threading.Thread(target=zadanieA)
t2 = threading.Thread(target=zadanieB)

t1.start()
t2.start()

t1.join()
t2.join()

print("Koniec udało się")