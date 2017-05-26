import os
import platform
import math

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'c5abc69d'.decode('hex')
P2P_PORT = 50603
ADDRESS_VERSION = 68
RPC_PORT = 50604
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            (yield helper.check_genesis_block(bitcoind, 'd8a2b2439d013a59f3bfc626a33487a3d7d27e42a3c9e0b81af814cd8e592f31')) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 100*100000000 * math.pow(0.99, (height-1999)/10080)
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('argon2d_hash').getHash(data, 80))
BLOCK_PERIOD = 300 # s
SYMBOL = 'UIS'
CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'unitus') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/unitus/') if platform.system() == 'Darwin' else os.path.expanduser('~/.unitus'), 'unitus.conf')
BLOCK_EXPLORER_URL_PREFIX = ''
ADDRESS_EXPLORER_URL_PREFIX = ''
TX_EXPLORER_URL_PREFIX = ''
SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//10000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.001e8
