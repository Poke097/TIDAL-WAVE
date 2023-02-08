import socket
import sys
import argparse
import pyfiglet
import colorama
from colorama import Fore
from ipwhois import IPWhois

colorama.init()

parser = argparse.ArgumentParser(description='Look up IP address and information for a given hostname')
parser.add_argument('hostname', type=str, help='Hostname to look up')
parser.add_argument('--output', type=str, help='File to save the results', default=None)
args = parser.parse_args()

ascii_banner = pyfiglet.figlet_format("DNS Index")
print(Fore.GREEN + ascii_banner.center(80, "-"))

if args.output:
    sys.stdout = open(args.output, 'w')

ip_address = socket.gethostbyname(args.hostname)

ip_info = IPWhois(ip_address)
result = ip_info.lookup_rdap()

print(f'{args.hostname} IP address is {ip_address}')
print(f'Country: {result["asn_country_code"]}')
print(f'ISP: {result["asn_description"]}')
print(f'Network Name: {result["network"]["name"]}')
print(f'CIDR Range: {result["network"]["cidr"]}')
print(f'Handle: {result["network"]["handle"]}')
print(f'Start Address: {result["network"]["start_address"]}')
print(f'End Address: {result["network"]["end_address"]}')
