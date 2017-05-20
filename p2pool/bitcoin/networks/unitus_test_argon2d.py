import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'c6abc79d'.decode('hex')
P2P_PORT = 60603
ADDRESS_VERSION = 130
RPC_PORT = 60604
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            (yield helper.check_genesis_block(bitcoind, '79b11e9472e5876fa6b6fac3efd46d63ee19e6f700d9048364e0b4ddeab0b58b')) and
            (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 1*100000000 >> (height + 1)//967680
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
