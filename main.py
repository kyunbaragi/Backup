from observable import Producer
from observer import ConsumerA
from observer import ConsumerB


if __name__ == '__main__':
    producer = Producer()

    # Register your consumer!
    ConsumerA(producer)
    ConsumerB(producer)

    producer.start()
