#!/usr/bin/env python3

"""
	File: pyBluezClient.py

	Install packages: 
		apt-get install bluez libbluetooth-dev

	Install python module: 
		pip3 install pybluez

	Show bluetooth devices:
		hciconfig -a
"""

import bluetooth
import os
import sys


def print_help():
	script_name = os.path.basename(__file__)
	print('USAGE: ' + script_name + ' <server_mac> <server_port> "message to send"')


def main(argv):

	if len(argv) < 4:
		print_help()
		exit(1)

	server_bt_mac  = argv[1]
	server_bt_port = int(argv[2])
	message = argv[3]

	server_bt_address = server_bt_mac, server_bt_port

	sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
	sock.connect(server_bt_address)

	sock.send(message)
	sock.close()


if __name__ == '__main__':
	main(sys.argv)
