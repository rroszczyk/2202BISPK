import threading
import time

semafor = threading.Semaphore(0)

zmienna = None

def producent():
    print("Jestem producentem, będę zamieszczał wynik w zmiennej")
    while True:
        global zmienna
        print("Produkcja w toku")
        time.sleep(5)
        zmienna = "wynik"
        print("Produkcja została zakończona - informujemy konsumenta")
        semafor.release()

def konsument():
    print("Jestem konsumentem, będę czekał na dane w zmiennej")
    while True:
        print("Czekam na dane od producenta")
        semafor.acquire()
        print(f"Uzyskałem dane: {zmienna}")


t1 = threading.Thread(target=producent)
t2 = threading.Thread(target=konsument)

t1.start()
t2.start()

t1.join()
t2.join()
