#!/usr/bin/env python3

import socket
import ssl
import requests

# -----------------------------
# ASCII Banner for Dishant Web Scanner
# -----------------------------
def print_banner():
    banner = r"""

██╗    ██╗███████╗██████╗     ███████╗███████╗ ██████╗██╗   ██╗██████╗ ██╗████████╗██╗   ██╗
██║    ██║██╔════╝██╔══██╗    ██╔════╝██╔════╝██╔════╝██║   ██║██╔══██╗██║╚══██╔══╝╚██╗ ██╔╝
██║ █╗ ██║█████╗  ██████╔╝    ███████╗█████╗  ██║     ██║   ██║██████╔╝██║   ██║    ╚████╔╝
██║███╗██║██╔══╝  ██╔══██╗    ╚════██║██╔══╝  ██║     ██║   ██║██╔══██╗██║   ██║     ╚██╔╝
╚███╔███╔╝███████╗██████╔╝    ███████║███████╗╚██████╗╚██████╔╝██║  ██║██║   ██║      ██║
 ╚══╝╚══╝ ╚══════╝╚═════╝     ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝   ╚═╝      ╚═╝

                        ***** Github : Dishant404 *****
                        Developed by: https.dishant.ceh
                        SCANNER - Web Security Tool
    """
    print(banner)

# -----------------------------
# 1. Check Security Headers
# -----------------------------
def check_headers(url):
    print("\n[+] Checking Security Headers...\n")
    try:
        response = requests.get(url)
        headers = response.headers

        security_headers = [
            "Content-Security-Policy",
            "Strict-Transport-Security",
            "X-Content-Type-Options",
            "X-Frame-Options",
            "X-XSS-Protection"
        ]

        for header in security_headers:
            if header in headers:
                print(f"[✔] {header} is present")
            else:
                print(f"[✘] {header} is missing")

    except Exception as e:
        print("Error:", e)

# -----------------------------
# 2. Port Scanner
# -----------------------------
def scan_ports(host):
    print("\n[+] Scanning Common Ports...\n")
    ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 8080]

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"[OPEN] Port {port}")
        sock.close()

# -----------------------------
# 3. SSL Certificate Check
# -----------------------------
def check_ssl(host):
    print("\n[+] Checking SSL Certificate...\n")
    try:
        context = ssl.create_default_context()
        with socket.create_connection((host, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                cert = ssock.getpeercert()
                print("[✔] SSL Certificate Found")
                print("Issuer:", cert['issuer'])
                print("Valid Till:", cert['notAfter'])
    except:
        print("[✘] SSL not found or invalid")

# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":
    print_banner()
    target = input("Enter website (example: https://example.com): ")
    host = target.replace("https://", "").replace("http://", "").split("/")[0]

    check_headers(target)
    scan_ports(host)
    check_ssl(host)

    print("\n[✓] Scan Completed!")
