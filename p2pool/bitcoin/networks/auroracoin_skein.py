import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'fda4dc6c'.decode('hex')
P2P_PORT = 12340
ADDRESS_VERSION = 23
RPC_PORT = 12341
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            (yield helper.check_genesis_block(bitcoind, '2a8e100939494904af825b488596ddd536b3a96226ad02e0f7ab7ae472b27a8e'))
        ))
SUBSIDY_FUNC = lambda height: 25*100000000 >> (height + 1)//420000 if height <= 5450 else 125*10000000 >> (height + 1)//420000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('skeinhash').getPoWHash(data))
BLOCK_PERIOD = 5*61 # s
SYMBOL = 'AUR'
CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'auroracoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/auroracoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.auroracoin'), 'auroracoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://blockexplorer.auroracoin.eu/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://blockexplorer.auroracoin.eu/address/'
TX_EXPLORER_URL_PREFIX = 'http://blockexplorer.auroracoin.eu/tx/'
SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**26 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 0.001e8
