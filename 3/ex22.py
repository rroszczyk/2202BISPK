from math import sqrt
import time

def is_prime(x):
    if x < 2:
        print(f'{x} nie jest liczbą pierwszą')

    elif x == 2:
        print(f'{x} jest liczbą pierwszą')

    elif x % 2 == 0:
        print(f'{x} nie jest liczbą piewszą')

    else:
        limit = int(sqrt(x)) + 1
        for i in range(3, limit, 2):
            if x % i == 0:
                print(f'{x} nie jest liczbą pierwszą')
                return

        print(f'{x} jest liczbą pierwszą')

if __name__ == '__main__':
    t1 = time.time()
    is_prime(4353465364364362)
    is_prime(14364363463462)
    is_prime(9637529763296797)
    is_prime(1619)
    print(f"Czas wykonania synchronicznego {time.time() - t1}")
