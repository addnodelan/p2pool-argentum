About
-------------------------
This is a Myriadcoin customised version of P2Pool, forked directly from https://github.com/forrestv/p2pool.

All 5 of Myriadcoin's algorithms are supported and preconfigured, and Python modules for each are provided.

Requirements & Setup:
-------------------------
Generic:
* Myriadcoin >=0.9.2.12 (https://github.com/myriadcoin/myriadcoin/releases)
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

* SHA256d - myriad_sha256d
* Scrypt - myriad_scrypt
* Skein - myriad_skein
* Myr-Groestl - myriad_groestl
* Qubit - myriad_qubit

Ensure your myriadcoin daemon is configured with the same algorithm (via the algo= option in myriadcoin.conf).

To make your node accessible from the internet, open the following ports on your router (both the worker port and peer-2-peer port please!):

* SHA256d: Worker Port = 5578; Peer-2-Peer Port = 5577
* Scrypt: Worker Port = 5556; Peer-2-Peer Port = 5555
* Scrypt Low Hash: Worker Port = 5558; Peer-2-Peer Port = 5557
* Skein: Worker Port = 5589; Peer-2-Peer Port = 5588
* Myr-Groestl: Worker Port = 3333; Peer-2-Peer Port = 8889
* Qubit: Worker Port = 5567; Peer-2-Peer Port = 5566

Run for additional options:

    python run_p2pool.py --help

Front End
-------------------------
You can access the web front end via http://{ip-address-of-p2pool}:{worker-port}/static

The standard UI has been replaced with https://github.com/justino/p2pool-ui-punchy

Donations towards further development:
-------------------------
<<<<<<< HEAD
    1HNeqi3pJRNvXybNX4FKzZgYJsdTSqJTbk
=======
Run P2Pool with the "--net litecoin" option.
Run your miner program, connecting to 127.0.0.1 on port 9327.
Forward port 9338 to the host running P2Pool.

Litecoin's use of ports 9333 and 9332 conflicts with P2Pool running on
the Bitcoin network. To avoid problems, add these lines to litecoin.conf
and restart litecoind:
>>>>>>> upstream/master

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


