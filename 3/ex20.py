import random
import threading
import time
import queue

semafor = threading.Semaphore(0)
zdarzenie = threading.Event()

kolejka = queue.Queue()

def konsument():
    while True:
        semafor.acquire()
        print(f"Worker {threading.current_thread().name} rozpoczął pracę")
        print(f"Pobrano element {kolejka.get()}")
        zdarzenie.set()
        time.sleep(random.randint(1, 5))
        print(f"Worker {threading.current_thread().name} zakończył pracę")

def producent():
    for x in range(10):
        zdarzenie.clear()
        zmienna = f"Numer elementu: {x}"
        kolejka.put(zmienna)
        print("Producent wyprodukował element")
        semafor.release()
        zdarzenie.wait()
        print(f"element {zmienna} został wykorzystany")

t1 = threading.Thread(target=producent)
t21 = threading.Thread(target=konsument)
t22 = threading.Thread(target=konsument)
t21.daemon = True
t22.daemon = True

t1.start()
t21.start()
t22.start()

t1.join()
