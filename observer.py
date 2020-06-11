from abc import *
import os
import time


class Consumer(metaclass=ABCMeta):
    def __init__(self, producer, name, members):
        self.name = name
        self.members = members
        producer.add_consumer(self)

    def run(self):
        while True:
            print('Hello! I am {} of the PID {}'.format(self.name, os.getpid()))
            time.sleep(3)

    @abstractmethod
    def handle_event(self, event):
        pass


class ConsumerA(Consumer):
    def __init__(self, producer):
        name = 'ConsumerA'
        members = ['yunkyun.han', 'yunkyun.kim', 'yunkyun.lee']
        super().__init__(producer, name, members)

    def handle_event(self, event):
        print('Analyze ' + event)


class ConsumerB(Consumer):
    def __init__(self, producer):
        name = 'ConsumerB'
        members = ['dinggul.han', 'dinggul.kim']
        super().__init__(producer, name, members)

    def handle_event(self, event):
        print('Analyze ' + event)




