from argparse import ArgumentParser
from observable import Producer
from observer import ConsumerA
from observer import ConsumerB


def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument('--debug',
                        help='Run as DEBUG mode',
                        action='store_true', dest='debug', default=False)
    parser.add_argument('--cycle', type=int,
                        help='CYCLE of the event scanner',
                        action='store', dest='cycle_secs', default=30)
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    producer = Producer(args)

    # Register your consumer!
    ConsumerA(producer)
    ConsumerB(producer)

    producer.start()
