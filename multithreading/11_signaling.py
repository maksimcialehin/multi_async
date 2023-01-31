import random
import threading
import time
from enum import Enum


class BankTerminal:

    def __init__(self, port, ip_address):
        self.port = port
        self.ip_address = ip_address
        self.protocol = Protocol(port, ip_address)
        self.protocol.message_received += self.on_message_received

        self.operation_signal = threading.Event()

    def on_message_received(self, status):
        print(f'signaling for event:{status}')
        self.operation_signal.set()

    def purchase(self, amount):
        def process_purchase():
            purchase_op_code = 1
            self.protocol.send(purchase_op_code, amount)

            self.operation_signal.clear() # сбросить сигнал после возможного set, чтобы сработала боликровка на waiting
            print('\nwaiting for signal')
            self.operation_signal.wait()


class Event:

    def __init__(self):
        self.__handlers = []

    def __call__(self, *args, **kwargs):
        for f in self.__handlers:
            f(*args, **kwargs)

    def __iadd__(self, handler):
        self.__handlers.append(handler)
        return self

    def __isub__(self, handler):
        self.__handlers.remove(handlet)
        return self


class OperationStatus(Enum):
    FINISHED = 0
    FAULTED = 1


class Protocol:

    def __init__(self, port, ip_address):
        self.port = port
        self.ip_address = ip_address

        self.message_received = Event()
        self.set_ip_address()

    def set_ip_address(self):
        # calling 3rd party lib
        print('set ip and port once')
        time.sleep(0.2)
        return

    def send(self, op_code, parameter):
        def process_sending():
            print(f'Operation is in action with parameter={parameter}')
            result = self.process(op_code, parameter)
            self.message_received(result)

        t = threading.Thread(target=process_sending)
        t.start()

    def process(self, op_code, param):
        print(f'processing operation={op_code} with param={param}')
        time.sleep(2)

        # 3rd party lib response
        finished = random.randint(0, 1)
        return OperationStatus.FINISHED if finished == 0 else OperationStatus.FAULTED
