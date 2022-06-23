#!/usr/bin/env python3


def main():
	with open('passwd') as f:
		passwd_content = f.readlines()

	with open('shadow') as f:
		shadow_content = f.readlines()

	users = {}

	for i in shadow_content:
		if i.split(':')[1].startswith('$'):
			users[i.split(':')[0]] = i.split(':')[1]

	with open('combined', 'w') as f:
		for i in passwd_content:
			if i.split(':')[0] in users.keys():
				f.write(i.replace(':x:', ':' + users[i.split(':')[0]] + ':'))


main()
