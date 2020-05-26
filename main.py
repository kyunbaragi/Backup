from observable import Observable
from observer import ChildObserver


if __name__ == '__main__':
    producer = Observable()

    consumer_1 = ChildObserver(producer, 'Tom')
    consumer_2 = ChildObserver(producer, 'Jerry')
    consumer_3 = ChildObserver(producer, 'Jin')

    producer.start()


