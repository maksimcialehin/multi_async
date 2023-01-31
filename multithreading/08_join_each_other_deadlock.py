import threading
import time


def f1():
    print('Running 1st thread\n')
    print('f1 join f2\n')
    time.sleep(2)
    t2.join()

    print('f1 sleeps')
    time.sleep(5)
    print('end of f1')


def f2():
    print('Running 2nd thread\n')
    print('f2 join f1\n')
    time.sleep(2)
    t1.join()

    print('f2 sleeps')
    time.sleep(5)
    print('end of f2')


if __name__ == '__main__':
    t1 = threading.Thread(target=f1)
    t2 = threading.Thread(target=f2)

    t1.start()
    t2.start()
