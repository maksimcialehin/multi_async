import threading
import time


# shared data
a = 5
b = 5

a_lock = threading.Lock()
b_lock = threading.Lock()


def thread1_calc():
    global a, b

    print('Thread 1 acquiring lock a')
    a_lock.acquire()
    time.sleep(5)

    print('Thread 1 acquiring lock b')
    b_lock.acquire()
    time.sleep(5)

    a += 5
    b += 6

    print('Thread 1 release both locks')
    a_lock.release()
    b_lock.release()


def thread2_calc():
    global a, b

    print('Thread 2 acquiring lock b')
    b_lock.acquire()
    time.sleep(5)

    print('Thread 2 acquiring lock a')
    a_lock.acquire()
    time.sleep(5)

    a += 55
    b += 66

    print('Thread 2 release both locks')
    b_lock.release()
    a_lock.release()


if __name__ == '__main__':
    print('started main')

    t1 = threading.Thread(target=thread1_calc)
    t1.start()

    t2 = threading.Thread(target=thread2_calc)
    t2.start()
