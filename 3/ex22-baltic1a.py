from math import sqrt

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
    is_prime(2)
    is_prime(12)
    is_prime(7)
    is_prime(61)
    is_prime(425)

    is_prime(1619)
