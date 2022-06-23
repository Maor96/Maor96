#!/usr/bin/env python3


def convert(seconds):
	'''
	Takes an integer and returns a string that represents the time since midnight.

	Parameters:
		seconds (int): Seconds since midnight

	Returns:
		time (str): Time since midnight in HH:MM:SS format
	'''

	if not 0 <= seconds <= 86400:
		return 'Error'
	
	minutes = int(seconds / 60)
	seconds -= minutes * 60

	hours = int(minutes / 60)
	minutes -= hours * 60

	return str(hours) + ':' + str(minutes) + ':' + str(seconds)


def main():
	print(convert(9879))


main()
