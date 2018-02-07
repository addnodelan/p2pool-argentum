from p2pool.bitcoin import networks

PARENT = networks.nets['argentum_scrypt']
SHARE_PERIOD = 15 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 40 # blocks
IDENTIFIER = '7c9f019d26641a2b'.decode('hex')
PREFIX = '15eca1b24ce3bf2b'.decode('hex')
P2P_PORT = 13585
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 9555
BOOTSTRAP_ADDRS = '45.76.112.155 45.76.240.8'.split(' ')
#ANNOUNCE_CHANNEL = '#p2pool-ltc'
VERSION_CHECK = lambda v: None if 1090000 <= v else 'Argentum version too old. Upgrade to 4.14.3 or newer!'
VERSION_WARNING = lambda v: None
