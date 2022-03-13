import time
from multiprocessing import Process, current_process
import os


def a():
    pName = current_process().name
    print(f"Startuje proces {pName}")
    print(f"Identyfikator aktualnego procesu to: {os.getpid()}")
    time.sleep(10)
    print(f"Zatrzymuje proces {pName}")

def b():
    pName = current_process().name
    print(f"Startuje proces {pName}")
    print(f"Identyfikator aktualnego procesu to: {os.getpid()}")
    time.sleep(5)
    print(f"Zatrzymuje proces {pName}")


if __name__ == '__main__':
    print(f"Identyfikator aktualnego procesu to: {os.getppid()}")
    p1 = Process(name="Worker 1", target=a)
    p1.daemon = True
    p2 = Process(name="Worker 2", target=b)

    p1.start()
    p2.start()

    #p1.join()
    print(f"Sprawdzam czy proces p1 nadal działa {p1.is_alive()}")

    p2.join()

    print("Zakończyło się działanie programu")