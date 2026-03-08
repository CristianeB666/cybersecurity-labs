import socket
import ipaddress
from datetime import datetime

networks = [
    "10.10.10.0/24",
    "10.20.10.0/24",
    "10.30.10.0/24"
]

ports = range(1, 65536)
timeout = 0.5

print(f"Iniciando teste de segmentação: {datetime.now()}\n")

def test_connection(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((str(ip), port))
        sock.close()
        return result == 0
    except:
        return False

for network in networks:

    print(f"\nTestando rede: {network}")

    net = ipaddress.ip_network(network)

    for ip in net.hosts():
        for port in ports:

            if test_connection(ip, port):
                print(f"[ACESSÍVEL] {ip}:{port}")
