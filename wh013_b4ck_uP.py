#!/usr/bin/python3
from os import system as run
import sys
import time

print("backing up /dev/sda7 to an external drive in gzip format.")
print("the program will run dd if=/dev/sda7 conv=sync,noerror bs=64k | gzip > /media/root/device_name/xxx.gz")
time.sleep(0.5)
print("[i] if you want to alter the drive you wish to back up, hit 'c', by default, we assume Yes.")
time.sleep(1.8)
init_ask = input("do you really want to undergo the full system backup? (Y *| n| c): ")
time.sleep(0.5)
if init_ask == "" or init_ask in ["y", "Y"]:
	print("executing a full system backup now...")
	print("executing dd (DATA DUPLICATOR) command...")
	time.sleep(1)
#	run("dd if=/dev/sda7 conv=sync,noerror status=progress bs=64k| gzip > /media/root/device_name/xxx.gz")

elif init_ask in ["c", "C"]:
	infile = input("enter the full path of drive you wish to backup. e.g. /dev/sdaX: ")
	outfile = input("enter the full path of the location where you wish to backup your drive with gz filename.\n e.g. \"/media/root/usb_dev/backup.img.gz\": ")
	print("conducting full backup of {} --> {}. it will likely take a long time.".format(infile, outfile))
	time.sleep(1)
#	run("dd if={} conv=sync,noerror status=progress bs=64k | gzip > {}".format(infile, outfile))	

else:
	print("exiting...")
	sys.exit(0)

