import threading


def filozof(left, right):
    while True:
        with left:
            with right:
                print(f"Filozof numer {threading.current_thread()} je")


liczbaWidelcy = 5
widelce = [threading.Lock() for n in range(liczbaWidelcy)]

filozofowie = [threading.Thread(target=filozof, args=(widelce[n], widelce[(n + 1) % liczbaWidelcy])) for n in range(liczbaWidelcy)]

for filozof in filozofowie:
    filozof.start()