import subprocess
import threading
import socket
from utils import run_command

def enumerate_subdomains(domain):
    print(f"[+] Enumerating subdomains for {domain} ...")
    # Using subfinder as example; must be installed on system
    cmd = f"subfinder -d {domain} -silent"
    subs = run_command(cmd)
    return subs.splitlines()

def check_live_domains(domains):
    print("[+] Checking live domains using httpx ...")
    domain_str = "\n".join(domains)
    with open("temp_domains.txt", "w") as f:
        f.write(domain_str)
    cmd = "httpx -l temp_domains.txt -silent"
    live = run_command(cmd).splitlines()
    return live

open_ports = []
lock = threading.Lock()

def scan_port(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        sock.close()
        if result == 0:
            with lock:
                open_ports.append(port)
    except:
        pass

def port_scan(ip, ports=None):
    if ports is None:
        ports = [21, 22, 80, 443, 8080, 8443, 3306]
    global open_ports
    open_ports = []
    threads = []
    for port in ports:
        t = threading.Thread(target=scan_port, args=(ip, port))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    return open_ports
