from mylogger import Log
from config import CONFIG
from argparse import ArgumentParser
from observable import Producer
from observer import ConsumerA
from observer import ConsumerB


def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument('--debug',
                        help='Run as DEBUG mode',
                        action='store_true', dest='debug',
                        default=CONFIG['DEFAULT']['DEBUG'])
    parser.add_argument('--cycle',
                        help='CYCLE of the event scanner',
                        type=int, action='store', dest='cycle_secs',
                        default=CONFIG['DEFAULT']['CYCLE'])
    return parser.parse_args()


if __name__ == '__main__':
    Log.init(level=Log.DEBUG)

    args = parse_arguments()
    producer = Producer(args)

    # Register your consumer!
    ConsumerA(producer)
    ConsumerB(producer)

    producer.start()
