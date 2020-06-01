#!/usr/bin/env python3
"""
Script that parses the tcpdump logfile for MAC addresses and compares them
against a pre-existing dictionary of known MAC addresses to see if new address
is on the network and logs this if so. 

Flow:
Pull in knowns --> check log for new --> compare against knowns -->
if known ignore --> if not known, add to knowns -->
(bonus) nmap to check OS details
"""

# Imports
import sys
import os

# Global variables
recAddr = {}

# Populates 'recAddr' with known MAC addresses
def known(filename="trustedMAC.txt"):
	with open(filename, "r") as cache:
		lines = cache.readlines()
		for index, address in enumerate(lines):
			address = address.split()
			recAddr[address[0]] = [address[2]]
# Writes new MAC's to trusted MAC file and records timestamps
def compare(addr, stamp):
	isDone = False
	for oldAddr in recAddr:
		if isDone == True: 
			break
		if oldAddr == addr:
			recAddr[addr].append(stamp)
			isDone = True
	if isDone == True:
		return
	f = open("trustedMAC.txt", "a")
	f.write(addr + " :: unknown\n")
	f.close()
	if addr in recAddr:
		recAddr[addr].append(stamp)
	else:
		recAddr[addr] = [stamp]

# Scans TCP dump for new MAC addresses and adds to 
def scan(filename="log.txt"):
	with open(filename, "r") as cache:
		lines = cache.readlines()
		for index, newAddress in enumerate(lines):
			newAddress = newAddress.split()
			try:
				compare(newAddress[1],newAddress[0])
			except:
				continue

def main():

	known()
	scan()
	for key in recAddr:
		print ("MAC ADDRESS:",key,"SYSTEM/TIMESTAMPS:", recAddr.get(key))


# A peaceful day, that is,
if __name__ == '__main__':
    main()
