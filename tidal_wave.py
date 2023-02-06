import os
import sys
import colorama
from colorama import Fore
import pyfiglet

colorama.init()

def main():
    print("Hello. Please make your choices below.".center(80, "-"))
    print(Fore.CYAN +
    """
     ____________________________
    /                           /\
   /        TIDAL WAVE        _/ /\
  /                          / \/
 /                           /\
/___________________________/ /
\___________________________\/
 \ \ \ \ \ \ \ \ \ \ \ \ \ \ \
    """)

    print("List of Attacks:")
    print("-" * 80)
    print("[1]. DNS Index")
    print("[2]. Port Guider! (Port Scanner)")
    print("[3]. Robo-Scrap (Robots.txt Web Crawler")
    print("[4]. Digital Storm (DDoS Attack Script)")

    try:
        selection = int(input("Choose Attack Number:"))
    except ValueError:
        print("Invalid Selection. Enter a number 1-4.")
        return

    if selection == 1:
        import dns_index
    elif selection == 2:
        import port_guider
    elif selection == 3:
        import robo_scrap
    elif selection == 4:
        import digital_storm
    else:
        print("Invalid Selection. Enter a number 1-4.")

if __name__ == '__main__':
    main()
