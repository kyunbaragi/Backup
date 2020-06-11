import os
import time
from multiprocessing import Process
from myrequests import MyRequests


class Producer:
    def __init__(self):
        self._consumers = []
        self._requests = MyRequests()

    def add_consumer(self, consumer):
        self._consumers.append(consumer)

    def start(self):
        self._fork_consumers()

        # TODO: Start scanner and result handler threads.
        while True:
            print('Hello! I am PRODUCER of the PID {}'.format(os.getpid()))
            time.sleep(1)

    def _fork_consumers(self):
        for consumer in self._consumers:
            proc = Process(target=consumer.run,
                           name=consumer.name,
                           daemon=True)
            proc.start()

    def _notify_events(self):
        for consumer in self._consumers:
            for member in consumer.members:
                events = self._requests.scan(member)
                if events:
                    # TODO: Put events into multiprocessing queue.
                    pass
