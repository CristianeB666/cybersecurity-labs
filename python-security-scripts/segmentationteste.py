import socket
import ipaddress
from datetime import datetime

# Redes que você quer testar
networks = [
    "10.10.10.0/24",   # Produção
    "10.20.10.0/24",   # HML
    "10.30.10.0/24",   # UAT
    "10.40.10.0/24"    # Automação
]

# Portas comuns para teste
ports = [22, 80, 443, 3389]

timeout = 1

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
