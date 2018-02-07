from p2pool.bitcoin import networks

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

PARENT = networks.nets['argentum_groestl']
SHARE_PERIOD = 15 # seconds
CHAIN_LENGTH = 24*60*60//15 # shares
REAL_CHAIN_LENGTH = 24*60*60//15 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 40 # blocks
IDENTIFIER = '157e689775ebc522'.decode('hex')
PREFIX = '313fd6e799574e83'.decode('hex')
P2P_PORT = 13583
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 9553
BOOTSTRAP_ADDRS = '45.76.112.155 45.76.240.8'.split(' ')
VERSION_CHECK = lambda v: None if 1090000 <= v else 'Argentum version too old. Upgrade to 4.14.3 or newer!'
ALGORITHM = 'Groestl'