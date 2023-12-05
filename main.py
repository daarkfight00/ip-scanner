import socket
import requests
import webbrowser
import time
import os
import colorama
from colorama import Fore
import sys
import platform

colorama.init()

operating_system = platform.system()

if operating_system == "Windows":
    clear_command = "cls"
else:
    clear_command = "clear"

print(r"""  ___  ________        ________  ________  ________  ________   ________   _______   ________     
|\  \|\   __  \      |\   ____\|\   ____\|\   __  \|\   ___  \|\   ___  \|\  ___ \ |\   __  \    
\ \  \ \  \|\  \     \ \  \___|\ \  \___|\ \  \|\  \ \  \\ \  \ \  \\ \  \ \   __/|\ \  \|\  \   
 \ \  \ \   ____\     \ \_____  \ \  \    \ \   __  \ \  \\ \  \ \  \\ \  \ \  \_|/_\ \   _  _\  
  \ \  \ \  \___|      \|____|\  \ \  \____\ \  \ \  \ \  \\ \  \ \  \\ \  \ \  \_|\ \ \  \\  \| 
   \ \__\ \__\           ____\_\  \ \_______\ \__\ \__\ \__\\ \__\ \__\\ \__\ \_______\ \__\\ _\ 
    \|__|\|__|          |\_________\|_______|\|__|\|__|\|__| \|__|\|__| \|__|\|_______|\|__|\|__|
                        \|_________|                                                             
                                                                                                 
                                                                                                                                                    """)

print(Fore.WHITE + "\t \t \t \t \t \t \t \t Developer: https://github.com/daarkfight00 ✔ \n ")
print(Fore.GREEN + "Questo software e' stato realizzato solo per scopo illustrativo, percio' non sono responsabile delle azioni che chiunque possa compiere con questo programma...")
print(Fore.CYAN + "\nThis software is for illustrative purposes only, so I am not responsible for the actions that anyone can perform with this program...")
messaggio = Fore.RED +"\n \n \t \t \t \t \t Please Don't Use It For illegal Activity  [X]\n \n"
for char in messaggio:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)
input(Fore.WHITE + "Press a key to continue")
os.system(clear_command)

def animated_header(ip, hostname=None):
    if hostname:
        header = f"\t \t \t Hostname: {Fore.YELLOW}{hostname}{Fore.RESET}\n"
    else:
        header = ""
    header += f"\t \t \t \t \t {Fore.YELLOW}Ip address selected = [ {ip} ]{Fore.RESET}"
    for char in header:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n")

def display_info(data):
    print(f"{Fore.CYAN}IP: {data['query']}")
    print(f"City: {data['city']}")
    print(f"Region: {data['regionName']}")
    print(f"Country: {data['country']}")
    print(f"ISP: {data['isp']}")
    print(f"Latitude: {data['lat']}")
    print(f"Longitude: {data['lon']}{Fore.RESET}")
    print(f"\n \nATTENTION!! The position is not very precise, ranging from (10 m to 100km)")

def scan_ip(ip):
    try:
        host_name = socket.gethostbyaddr(ip)
        print(f"{Fore.YELLOW}Hostname: {host_name[0]}{Fore.RESET}")
    except socket.herror:
        print(f"{Fore.YELLOW}Hostname not found.{Fore.RESET}")
        time.sleep(2)
        return

    try:
        print(f"{Fore.YELLOW}Fetching data... {Fore.RESET}", end="")
        sys.stdout.flush()
        time.sleep(1)
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        sys.stdout.write("\033[K")
        animated_header(ip, host_name[0])
        display_info(data)
    except requests.exceptions.RequestException:
        sys.stdout.write("\033[K")
        print("Unable to get location information.")

if __name__ == "__main__":
    while True:
        os.system(clear_command)
        print("0. Exit")
        print("1. Scan own IP")
        print("2. Scan specific IP")
        print("3. Open GitHub project")

        choice = input("Enter your choice: ")

        if choice == "0":
            break
        elif choice == "1":
            own_ip = requests.get('https://api64.ipify.org?format=json').json()['ip']
            os.system(clear_command)
            scan_ip(own_ip)
        elif choice == "2":
            target_ip = input("Enter target IP: ")
            os.system(clear_command)
            scan_ip(target_ip)
        elif choice == "3":
            print("Opening GitHub project...")
            webbrowser.open("https://github.com/daarkfight00", new=2)
        else:
            print("Invalid choice.")

        input("\rPress any key to continue...   ")
        another_scan = input("Scan another IP? [Y] [n] : ")
        if another_scan.lower() not in ["y", "", "Y"]:
            messaggio = f"{Fore.RED}\nDeveloper https://github.com/daarkfight00{Fore.RESET}\n"
            for char in messaggio:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.05)
            messaggio = f"{Fore.GREEN}Thanks for your use ;) {Fore.RESET}"
            for char in messaggio:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(3)
            os.system(clear_command)
            break