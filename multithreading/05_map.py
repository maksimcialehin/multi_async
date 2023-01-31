import concurrent.futures

from multithreading.count_three_sum import count_three_sum, read_ints
from multithreading.decorators import measure_time


if __name__ == '__main__':
    print('started main')

    ints = read_ints('..\\data\\1Kints.txt')

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        results = executor.map(count_three_sum, (ints, ints), ('t1', 't2'))

        for r in results:
            print(f'{r=}')

    print('ended main')