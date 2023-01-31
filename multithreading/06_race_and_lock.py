import concurrent.futures
import threading
import time


class BankAccount:
    def __init__(self):
        self.balance = 100  # shared resource
        self.lock_obj = threading.Lock()

    def update(self, transaction, amount):
        print(f'{transaction} started')

        with self.lock_obj:
            tmp_amount = self.balance
            tmp_amount += amount
            time.sleep(1)
            self.balance = tmp_amount

        # self.lock_obj.acquire()
        # tmp_amount = self.balance
        # tmp_amount += amount
        # time.sleep(1)
        # self.balance = tmp_amount
        # self.lock_obj.release()

        print(f'{transaction} ended')


if __name__ == '__main__':
    acc = BankAccount()
    print(f'Started main. Account balance = {acc.balance}')

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(acc.update, ('refill', 'withdraw'), (100, -200))

    print(f'Ended main. Account balance = {acc.balance}')
