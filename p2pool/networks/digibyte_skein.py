from p2pool.bitcoin import networks

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

PARENT = networks.nets['digibyte_skein']
SHARE_PERIOD = 15 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 50 # shares
SPREAD = 30 # blocks
IDENTIFIER = '48a4ebc31b798114'.decode('hex')
PREFIX = '5685a276c2dd71db'.decode('hex')
P2P_PORT = 5030
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 5031
BOOTSTRAP_ADDRS = 'nz.pool.geek.nz mine4free.noip.me'.split(' ')
VERSION_CHECK = lambda v: True
