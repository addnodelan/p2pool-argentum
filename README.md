About
-------------------------
This is an Argentum customised version of P2Pool, forked directly from https://github.com/forrestv/p2pool.

All 6 Argentum's algorithms (myr-groestl, argon2d, yescrypt, scrypt, sha256, lyra2re2) are supported and preconfigured, and Python modules for each are provided. No AUXPOW on Scrypt or SHA256 with P2Pool.

Requirements & Setup:
-------------------------
Generic:
* Argentum >=4.14.3 (https://github.com/argentumproject/argentum/releases)
* Python >=2.6 (https://www.python.org/downloads/)
* Zope.Interface >=3.8(https://pypi.python.org/pypi/zope.interface)
* Twisted >=10.0.0 (https://twistedmatrix.com/trac/wiki/Downloads)
* python-argparse (for Python =2.6)

To install the hash modules, go into each sub-folder within /hash_modules and run

    sudo python setup.py install

	
Running P2Pool:
-------------------------
To use P2Pool, you must be running your own local argentum daemon. For standard
configurations, using P2Pool should be as simple as:

    python run_p2pool.py --net {network_name}

Replace {network_name} with the following depending on the algorithm:

* Argon2d - argentum_argon2d
* Myr-Groestl - argentum_groestl
* Yescrypt - argentum_yescrypt
* Scrypt - argenum_scrypt
* Sha256d - argentum_sha256
* Lyra2re2 - argentum_lyra2re2

Ensure your argentum daemon is configured with the same algorithm (via the algo= option in argentum.conf).

To make your node accessible from the internet, open the following ports on your router (both the worker port and peer-2-peer port please!):

* Argon2d: Worker Port = 9552; Peer-2-Peer Port = 13582
* Myr-Groestl: Worker Port = 9553; Peer-2-Peer Port = 13583
* Yescrypt: Worker Port = 9554; Peer-2-Peer Port = 13584
* Scrypt: Worker Port = 9555; Peer-2-Peer Port = 13585
* Sha256: Worker Port = 9556; Peer-2-Peer Port = 13586
* Lyra2re2: Worker Port = 9557; Peer-2-Peer Port = 13587

Run for additional options:

    python run_p2pool.py --help

Front End
-------------------------
You can access the web front end via http://{ip-address-of-p2pool}:{worker-port}/static

The standard UI has been replaced with https://github.com/justino/p2pool-ui-punchy

Donations towards further development:
-------------------------
    1HNeqi3pJRNvXybNX4FKzZgYJsdTSqJTbk

Official wiki:
-------------------------
https://en.bitcoin.it/wiki/P2Pool

Sponsors:
-------------------------
Thanks to:

* The Bitcoin Foundation for its generous support of P2Pool
* The Litecoin Project for its generous donations to P2Pool

License:
-------------------------
[Available here](LICENSE)


