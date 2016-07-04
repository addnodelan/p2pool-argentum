import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = '01f555a4'.decode('hex')
P2P_PORT = 20888
ADDRESS_VERSION = 88
RPC_PORT = 20889
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            (yield helper.check_genesis_block(bitcoind, '0000017ce2a79c8bddafbbe47c004aa92b20678c354b34085f62b762084b9788')) and
            (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 1000*100000000 >> (height + 1)//967680
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('yescrypt_hash').getHash(data, 80))
BLOCK_PERIOD = 300 # s
SYMBOL = 'XMY'
CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'myriadcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/myriadcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.myriadcoin'), 'myriadcoin.conf')
BLOCK_EXPLORER_URL_PREFIX = ''
ADDRESS_EXPLORER_URL_PREFIX = ''
TX_EXPLORER_URL_PREFIX = ''
SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//10000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.001e8
