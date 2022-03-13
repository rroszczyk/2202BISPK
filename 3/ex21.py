import multiprocessing

class Worker():
    def __init__(self, x):
        self.x = x

    def process(self):
        pName = multiprocessing.current_process().name
        print(f"Startujemy proces: {pName} dla zmiennej wejściowej: {self.x}")

def work(kolejka):
    while True:
        worker = kolejka.get()
        worker.process()

if __name__ == '__main__':
    kolejka = multiprocessing.Queue()

    p = multiprocessing.Process(target=work, args=(kolejka, ))
    p.start()

    kolejka.put(Worker(10))
    kolejka.put(Worker(5))
    kolejka.put(Worker(17))

    kolejka.close()
    kolejka.join_thread()

    p.join()
