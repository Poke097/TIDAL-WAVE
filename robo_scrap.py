import pyfiglet
import urllib.request
import io
import colorama
from colorama import Fore

colorama.init()

ascii_banner = pyfiglet.figlet_format("Robo - Scrap")
print(Fore.YELLOW + ascii_banner)

url = input("Please enter target URL:")

if not url.startswith("http://") and not url.startswith("https://"):
    url = "http://" + url

def get_robots_txt(url):
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'

    req = urllib.request.urlopen(path + "robots.txt", data=None)
    data = io.TextIOWrapper(req, encoding='utf-8')
    return data.read()

robots_txt = get_robots_txt(url)
lines = robots_txt.splitlines()

user_agents = []
disallows = []
for line in lines:
    if line.startswith("User-agent"):
        user_agent = line.split(":")[1].strip()
        user_agents.append(user_agent)
    elif line.startswith("Disallow"):
        disallow = line.split(":")[1].strip()
        disallows.append(disallow)

print("User-Agents:")
for user_agent in user_agents:
    print(f"- {user_agent}")

print("Disallows:")
for disallow in disallows:
    print(f"- {disallow}")