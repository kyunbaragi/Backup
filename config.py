import configparser

config = configparser.ConfigParser()
config.read('config.ini')

# Singleton pattern with config.py module,
# It is guaranteed to read the config file once.
CONFIG = {
    'ACCOUNT': {
        'ID': config.get('ACCOUNT', 'ID', fallback=None),
        'PASSWORD': config.get('ACCOUNT', 'PASSWORD', fallback=None)
    },
    'DEFAULT': {
        'DEBUG': config.getboolean('DEFAULT', 'DEBUG', fallback=False),
        'CYCLE': config.getint('DEFAULT', 'CYCLE', fallback=60)
    }
}


