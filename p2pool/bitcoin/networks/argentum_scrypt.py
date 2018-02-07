import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'fbc1b8dc'.decode('hex')
P2P_PORT = 13580
ADDRESS_VERSION = 23
RPC_PORT = 13581
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            (yield helper.check_genesis_block(bitcoind, '88c667bc63167685e4e4da058fffdfe8e007e5abffd6855de52ad59df7bb0bb2')) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 3*100000000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 270 # s
SYMBOL = 'ARG'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Argentum') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Argentum/') if platform.system() == 'Darwin' else os.path.expanduser('~/.argentum'), 'argentum.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://chainz.cryptoid.info/arg/block.dws?'
ADDRESS_EXPLORER_URL_PREFIX = 'https://chainz.cryptoid.info/arg/address.dws?'
TX_EXPLORER_URL_PREFIX = 'https://chainz.cryptoid.info/arg/tx.dws?'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.03e8
