import threading


# lock_obj = threading.Lock()
lock_obj = threading.RLock()

print('Acquire 1st time')
lock_obj.acquire()

print('Acquire 2st time')
lock_obj.acquire()

print('Releasing')
lock_obj.release()
