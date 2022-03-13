import time

start = time.perf_counter()

def countDown(name, delay):
    indents = (ord(name) - ord('A')) * '\t'

    n = 3
    while n:
        time.sleep(delay)

        duration = time.perf_counter() - start
        print('-' * 40)
        print('%.4f \t%s%s = %i' % (duration, indents, name, n))

        n -= 1

countDown('A', 2)
countDown('B', 1)
countDown('C', 0.5)

