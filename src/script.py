import scapy.all as scapy

def send_ping(destination):
    print("----- INVIO PING A", destination, " -----")
    res = scapy.sr(scapy.IP(dst=destination)/scapy.ICMP(), timeout=4) # Invio echo request
    print("--- RISULTATI: ---")
    for r in res:
        r.show()
    print()

def send_tcp_syn(destination, port):
    print("----- INVIO SYN A", destination, ", PORTA", port, "-----")
    res = scapy.sr(scapy.IP(dst=destination)/scapy.TCP(dport=port,flags="S"), timeout=4) # Invio segmento TCP con flag S (SYN) attivo
    print("--- RISULTATI: ---")
    for r in res:
        r.show()
    print()

send_ping("google.com")
#send_ping("8.8.8.8")
#send_tcp_syn("google.com", 80)