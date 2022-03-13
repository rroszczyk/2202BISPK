import threading
import time
from multiprocessing import Pool

licznik = 100000000

def countDown(n):
    while n > 0:
        n -= 1

if __name__ == '__main__':

    start = time.time()
    countDown(licznik)

    print(f"Czas wykonania obliczeń jednowątkowo: {time.time() - start}")

    t1 = threading.Thread(target=countDown, args=(licznik // 2, ))
    t2 = threading.Thread(target=countDown, args=(licznik // 2, ))

    start = time.time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"Czas wykonania obliczeń wielowątkowo: {time.time() - start}")

    pool = Pool(processes=2)
    start = time.time()

    pool.apply_async(countDown, args=(licznik // 2, ))
    pool.apply_async(countDown, args=(licznik // 2,))

    pool.close()
    pool.join()
    print(f"Czas wykonania obliczeń na wielu procesach: {time.time() - start}")