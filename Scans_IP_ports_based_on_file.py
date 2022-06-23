#!/usr/bin/env python3


from socket import socket


def get_ports():
	ports = []

	with open('ports.txt') as f:
		for i in f.readlines():
			ports.append(int(i.split()[1].split('/')[0]))

	return ports


def main():
	ports = get_ports()

	target = input('Enter target IP address: ')
	ports_to_scan = int(input('How many ports to scan: '))


	for i in range(ports_to_scan):
		s = socket()

		try:
			s.connect((target, ports[i]))

			s.close()
		except ConnectionRefusedError:
			continue

		print('Port', ports[i], 'is open')


main()
