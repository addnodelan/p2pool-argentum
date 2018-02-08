from p2pool.bitcoin import networks

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

PARENT = networks.nets['argentum_sha256']
SHARE_PERIOD = 15 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 40 # blocks
IDENTIFIER = '52b2a82e80126f49'.decode('hex')
PREFIX = '720089174edc7a34'.decode('hex')
P2P_PORT = 13586
MIN_TARGET = 0
MAX_TARGET = 2**256//2**32 - 1
PERSIST = False
WORKER_PORT = 9556
BOOTSTRAP_ADDRS = '45.76.112.155 45.76.240.8'.split(' ')
#ANNOUNCE_CHANNEL = '#p2pool'
VERSION_CHECK = lambda v: None if 1090000 <= v else 'Argentum version too old. Upgrade to 4.14.3 or newer!'
VERSION_WARNING = lambda v: None
MINIMUM_PROTOCOL_VERSION = 1500
ALGORITHM = 'Sha256'