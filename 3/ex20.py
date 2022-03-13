import random
import threading
import time

semafor = threading.Semaphore(0)
zdarzenie = threading.Event()

# zamiast zmiennej należy użyć kolejki...
zmienna = None

def konsument():
    while True:
        semafor.acquire()
        print(f"Worker {threading.current_thread().name} rozpoczął pracę")
        time.sleep(random.randint(1, 5))
        print(f"Worker {threading.current_thread().name} zakończył pracę")
        zdarzenie.set()

def producent():
    global zmienna
    for x in range(10):
        zdarzenie.clear()
        zmienna = f"Numer elementu: {x}"
        print("Producent wyprodukował element")
        semafor.release()
        zdarzenie.wait()
        print(f"element {zmienna} został wykorzystany")

t1 = threading.Thread(target=producent)
t2 = threading.Thread(target=konsument)
t2.daemon = True

t1.start()
t2.start()

t1.join()
