About
-------------------------
This is a Myriad customised version of P2Pool, forked directly from https://github.com/forrestv/p2pool.

All 3 of Myriad's non-merge-mined algorithms (myr-groestl, skein, qubit) are supported and preconfigured, and Python modules for each are provided.

Requirements & Setup:
-------------------------
Generic:
* Myriadcoin >=0.9.2.16 (https://github.com/myriadcoin/myriadcoin/releases)
* Python >=2.6 (https://www.python.org/downloads/)
* Zope.Interface >=3.8(https://pypi.python.org/pypi/zope.interface)
* Twisted >=10.0.0 (https://twistedmatrix.com/trac/wiki/Downloads)
* python-argparse (for Python =2.6)

To install the hash modules, go into each sub-folder within /modules and run

    su python setup.py install

	
Running P2Pool:
-------------------------
To use P2Pool, you must be running your own local myriadcoin daemon. For standard
configurations, using P2Pool should be as simple as:

    python run_p2pool.py --net {network_name}

Replace {network_name} with the following depending on the algorithm:

* Myr-Groestl - myriad_groestl
* Skein - myriad_skein
* Qubit - myriad_qubit

Ensure your myriad daemon is configured with the same algorithm (via the algo= option in myriadcoin.conf).

To make your node accessible from the internet, open the following ports on your router (both the worker port and peer-2-peer port please!):

* Myr-Groestl: Worker Port = 5545; Peer-2-Peer Port = 5544
* Skein: Worker Port = 5589; Peer-2-Peer Port = 5588
* Qubit: Worker Port = 5567; Peer-2-Peer Port = 5566

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


