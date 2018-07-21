pyBluez Client and Server
=========================

Client and Server RFCOMM written in Python

What you need
-------------

Install the next packages.

`sudo apt-get install bluez libbluetooth-dev`

Install python **pybluez** module

`pip3 install pybluez`

Server
------

Show the bluetooth devices.

`hciconfig -a`

Configure the bluetooth device

`hciconfig hci0 piscan`

Run the server.

`python3 pyBluez/pyBluezServer.py **<server_port_number>**`

Client
------

Send message from the client to the server.

`python3 pyBluez/pyBluezClient.py **<mac_server>** **<server_port_number>** **<"Message to send">**`

