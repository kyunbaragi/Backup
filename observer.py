from abc import *
from mylogger import Log


class Consumer(metaclass=ABCMeta):
    def __init__(self, producer, name, members):
        self.name = name
        self.members = members

        # Register 'this' new observer.
        producer.add_consumer(self)

    def run(self, event_queue, result_queue):
        Log.d('Consumer', 'Hello! I am {}'.format(self.name))
        while True:
            # Use one-way blocking queue,
            # You don't need to handle process scheduling.
            event = event_queue.get()
            result = self.handle_event(event)

            # Return result to Producer.
            result_queue.put(result)

    @abstractmethod
    def handle_event(self, event):
        pass


class ConsumerA(Consumer):
    def __init__(self, producer):
        name = 'ConsumerA'
        members = ['yunkyun.han', 'yunkyun.kim', 'yunkyun.lee']
        super().__init__(producer, name, members)

    def handle_event(self, event):
        Log.d('ConsumerA', 'Receive {}'.format(event.id))
        return None


class ConsumerB(Consumer):
    def __init__(self, producer):
        name = 'ConsumerB'
        members = ['dinggul.han', 'dinggul.kim']
        super().__init__(producer, name, members)

    def handle_event(self, event):
        Log.d('ConsumerB', 'Receive {}'.format(event.id))
        return None




