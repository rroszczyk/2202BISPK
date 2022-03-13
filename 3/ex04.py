import random
import threading
import time

counter = 0
counterLock = threading.Lock()

def funkcjaZBlokada():
    global counter

    with counterLock:
        currentCounter = counter
        time.sleep(random.randint(0, 1))
        counter = currentCounter + 1

def funkcjaBezBlokady():
    global counter

    currentCounter = counter
    time.sleep(random.randint(0, 1))
    counter = currentCounter + 1


threads = [threading.Thread(target=funkcjaZBlokada()) for i in range(20)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(f"Końcowa wartość licznika to {counter}")