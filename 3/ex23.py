import time
from math import sqrt
import asyncio

async def is_prime(x):
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


async def main():
    t1 = loop.create_task(is_prime(4353465364364362))
    t2 = loop.create_task(is_prime(14364363463462))
    t3 = loop.create_task(is_prime(9637529763296797))
    t4 = loop.create_task(is_prime(1619))

    await asyncio.wait([t1, t2, t3, t4])


if __name__ == '__main__':

    t1 = time.time()
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
    print(f"Czas wykonania asynchronicznego {time.time() - t1}")

