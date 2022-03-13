import random
import threading
import time

zdarzenie = threading.Event()

def konsument():
    print("Jestem konsumentem będę potrzebował informacji o ropoczęciu pracy")
    zdarzenie.wait()
    print(f"Jestem konsumentem: {threading.current_thread().name} mogę zacząć pracę")
    time.sleep(random.randint(1,10))
    print(f"Praca zakończona przez konsumenta: {threading.current_thread().name}")


def informuj():
    print("Informacja dla konsumentów, że mogą rozpocząć pracę")
    time.sleep(10)
    print("Odblokowanie konsumentów")
    zdarzenie.set()


t1 = threading.Thread(target=konsument)
t2 = threading.Thread(target=konsument)
t3 = threading.Thread(target=konsument)
t4 = threading.Thread(target=konsument)


t1.start()
t2.start()
t3.start()
t4.start()

informuj()

t1.join()
t2.join()
t3.join()
t4.join()

