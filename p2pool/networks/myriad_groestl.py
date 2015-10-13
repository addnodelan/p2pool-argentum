from p2pool.bitcoin import networks

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

PARENT = networks.nets['myriad_groestl']
SHARE_PERIOD = 15 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 60 # blocks
IDENTIFIER = 'fafa54457667eeee'.decode('hex')
PREFIX = 'fa6754ee45ee76fa'.decode('hex')
P2P_PORT = 8889
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 3333
BOOTSTRAP_ADDRS = 'birdspool.no-ip.org nz.nutty.one mine4free.noip.me'.split(' ')
VERSION_CHECK = lambda v: None if 90216 <= v else 'Myriad version too old. Upgrade to 0.9.2.16 or newer!'
