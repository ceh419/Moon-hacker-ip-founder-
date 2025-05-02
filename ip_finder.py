import socket

def find_ip():
    hostname = input("Enter website URL (e.g. google.com): ")
    try:
        ip = socket.gethostbyname(hostname)
        print(f"IP address of {hostname} is: {ip}")
    except socket.gaierror:
        print("Invalid URL or no internet connection.")

if __name__ == "__main__":
    find_ip()
