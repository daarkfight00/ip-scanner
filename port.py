import socket
from colorama import Fore

def scan_port(target_host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((target_host, port))
        print(f"{Fore.RED}Port {port} is open{Fore.RESET}")
        s.close()
    except (socket.timeout, ConnectionRefusedError):
        pass
