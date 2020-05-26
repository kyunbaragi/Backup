import os
import time
from multiprocessing import Process
from simplerequests import SimpleRequests


class Observable:
    def __init__(self):
        self.observers = []
        self.child_process = []
        self.requests = SimpleRequests()

    def register_observer(self, o):
        self.observers.append(o)

    def unregister_observer(self, o):
        i = self.observers.index(o)
        self.observers.remove(i)

    def fork_observers(self):
        for o in self.observers:
            proc = Process(target=o.run, name=o.name, daemon=True)
            self.child_process.append(proc)
            proc.start()

        # for proc in self.child_process:
        #     proc.join()

    def iterate_cycle(self):
        for o in self.observers:
            group_issues = []
            for member in o.members:
                member_issues = self.requests.scan(member)
                if member_issues:
                    group_issues.append(member_issues)

            # Call observer's callback
            o.update(group_issues)

    def start(self):
        self.fork_observers()

        while True:
            print('Hello! I am PRODUCER of the PID {}'.format(os.getpid()))
            time.sleep(1)





