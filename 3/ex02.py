import threading
import time

def CountDown(name, count):
    while count > 0:
        print(f"{name} odliczam: {count}")
        count -= 1
        time.sleep(1)


t1 = threading.Thread(target=CountDown, args=("A", 5,))
t2 = threading.Thread(target=CountDown, args=("B", 15,))
t3 = threading.Thread(target=CountDown, args=("C", 10,))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

CountDown("M", 25)
