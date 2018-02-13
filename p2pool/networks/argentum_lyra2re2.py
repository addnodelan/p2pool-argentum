from p2pool.bitcoin import networks

PARENT = networks.nets['argentum_lyra2re2']
SHARE_PERIOD = 15 # seconds
CHAIN_LENGTH=  24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 40 # blocks
IDENTIFIER = '34f951cce036625a'.decode('hex')
PREFIX = '41e2060e323299d1'.decode('hex')
P2P_PORT = 13587
MIN_TARGET = 4
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 9557
BOOTSTRAP_ADDRS = '45.76.240.8'.split(' ')
VERSION_CHECK = lambda v: None if 1090000 <= v else 'Argentum version too old. Upgrade to 4.14.3 or newer!'
ALGORITHM = 'Lyra2re2'