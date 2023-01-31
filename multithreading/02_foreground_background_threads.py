import threading

from multithreading.count_three_sum import count_three_sum, read_ints


if __name__ == '__main__':
    print('started main')

    ints = read_ints('..\\data\\1Kints.txt')
    t1 = threading.Thread(target=count_three_sum, kwargs=dict(ints=ints), daemon=True)
    t1.start()

    print('what are you waiting for?')
    t1.join()
    print('ended main')
