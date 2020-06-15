import os
import time
from multiprocessing import Process
from multiprocessing import Queue
from threading import Thread
from myrequests import MyRequests


class Producer:
    def __init__(self, args):
        self._args = args

        self._consumers = {}
        self._event_queues = {}         # Events from Producer to Consumer
        self._result_queue = Queue()    # Results from Consumer to Producer

        self._requests = MyRequests()

    def add_consumer(self, consumer):
        self._consumers[consumer.name] = consumer
        self._event_queues[consumer.name] = Queue()

    def remove_consumer(self, consumer):
        del self._consumers[consumer.name]
        del self._event_queues[consumer.name]
        # TODO: Should kill consumer process?

    def start(self):
        self._fork_consumers()

        # In the Producer process...
        Thread(target=self._runnable_event_scanner).start()
        Thread(target=self._runnable_result_handler).start()

    def _fork_consumers(self):
        for c in self._consumers.values():
            event_queue = self._event_queues[c.name]
            result_queue = self._result_queue
            proc = Process(target=c.run, name=c.name,
                           args=(event_queue, result_queue,),
                           daemon=True)
            proc.start()

    def _runnable_event_scanner(self):
        while True:
            # one cycle++
            for c in self._consumers.values():
                event_queue = self._event_queues[c.name]
                for member in c.members:
                    # TODO: Create virtual test logic like real scenario.
                    # event_ids = self._requests.scan_events(member)

                    event_ids = ['EVENT_0', 'EVENT_1']
                    if event_ids:
                        for event_id in event_ids:
                            event = self._requests.construct_event(event_id)
                            event_queue.put(event)
            # one cycle--

            time.sleep(self._args.cycle_secs)

    def _runnable_result_handler(self):
        while True:
            result = self._result_queue.get()
            print('[PID {}] Handle Result {}'.format(os.getpid(), result))
