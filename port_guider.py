# Importing required modules
import socket
import sys
import argparse
from datetime import datetime
import threading
import pyfiglet
import concurrent.futures
import colorama
from colorama import Fore

# Initializing colorama for terminal colors
colorama.init()

# Setting up a lock for printing results
print_lock = threading.Lock()

# Creating an ASCII art banner for cool colors :D
ascii_banner = pyfiglet.figlet_format("Port Guider!")
print(Fore.CYAN + ascii_banner)

# Setting up argument parser to parse command line arguments. This will help guide people on how to use my program!
parser = argparse.ArgumentParser(description='Scan a given IP for open ports')
parser.add_argument('--ip', type=str, help='IP address to scan', required=True)
parser.add_argument('--start-port', type=int, help='Starting port to scan', default=1)
parser.add_argument('--end-port', type=int, help='Ending port to scan', default=1000)
parser.add_argument('--output', type=str, help='File to save the results', default=None)
args = parser.parse_args()

# Function to scan a single port
def scan(ip, port):
    # Creating a socket
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Setting a timeout of 1 second
    scanner.settimeout(1)
    try:
        # Connecting to the target IP and port
        scanner.connect((ip, port))
        # Closing the socket after a successful connection
        scanner.close()
        with print_lock:
            # Printing the port as open
            print(Fore.WHITE + f"[{port}]" + Fore.GREEN + "Open")
    except:
        # If connection fails, do nothing and move on to the next port
        pass

# Redirecting the output to a file if --output argument is provided
if args.output:
    sys.stdout = open(args.output, 'w')

# Printing the start time of the scan
print("Scanning started at:" + str(datetime.now()))

# Running the scan with 100 worker threads
with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    for port in range(args.start_port - 1, args.end_port):
        executor.submit(scan, args.ip, port + 1)