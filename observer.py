from abc import *
import os
import time


class Observer(metaclass=ABCMeta):
    def __init__(self, producer, name):
        self.producer = producer
        self.name = name
        producer.register_observer(self)

    def run(self):
        while True:
            print('Hello! I am {} of the PID {}'.format(self.name, os.getpid()))
            time.sleep(3)

    @abstractmethod
    def update(self, issue):
        pass


class ChildObserver(Observer):
    def __init__(self, producer, name):
        super().__init__(producer, name)

    def update(self, issue):
        # Get contents of the issue which you want!.
        issue_id = issue.id
        issue_title = issue.title
        issue_desc = issue.description

        print('Analyze' + issue_id)




