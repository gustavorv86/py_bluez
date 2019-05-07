#!/usr/bin/env python3

"""
	File: pyBluezServer.py

	Install packages: 
		apt-get install bluez libbluetooth-dev

	Install python module: 
		pip3 install pybluez

	Show bluetooth devices:
		hciconfig -a
	
	Configure the bluetooth interface:
		hciconfig hci0 piscan
"""

import bluetooth
import os
import sys


def print_help():
	script_name = os.path.basename(__file__)
	print('USAGE: ' + script_name + ' <server_port>')


def main(argv):
	
	if len(argv) < 2:
		print_help()
		exit(1)
	
	server_bt_port = int(argv[1])
	
	server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

	server_bt_address = '', server_bt_port

	server_sock.bind(server_bt_address)
	server_sock.listen(1)

	while True:

		client_sock,address = server_sock.accept()
		print('Accepted connection from ', address)

		data = client_sock.recv(1024)
		print('Received: ' + data.decode('utf-8'))

		client_sock.close()
		
	server_sock.close()


if __name__ == '__main__':
	main(sys.argv)

