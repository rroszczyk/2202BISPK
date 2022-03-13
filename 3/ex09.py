import threading

class manager():
    def __init__(self, *locks):
        self.locks = sorted(locks, key=lambda x: id(x))

    def __enter__(self):
        for lock in self.locks:
            lock.acquire()

    def __exit__(self, type, value, tb):
        for lock in reversed(self.locks):
            lock.release()
        return False

def filozof(left, right):
    while True:
        with manager(left, right):
                print(f"Filozof numer {threading.current_thread().name} je")


liczbaWidelcy = 5
widelce = [threading.Lock() for n in range(liczbaWidelcy)]

filozofowie = [threading.Thread(target=filozof, args=(widelce[n], widelce[(n + 1) % liczbaWidelcy])) for n in range(liczbaWidelcy)]

for filozof in filozofowie:
    filozof.start()