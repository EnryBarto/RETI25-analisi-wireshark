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

def send_tcp_flags(destination, port):
    print("----- FLAG DISPONIBILI: -----")
    print("F - FIN")
    print("S - SYN")
    print("R - RST")
    print("P - PSH")
    print("A - ACK")
    print("U - URG")
    print("E - ECE")
    print("C - CWR")
    print("\nDigitare i caratteri dei flag da attivare (ad esempio \"SR\" per i flag SYN e RST)\n>", end=" ")
    flgs = input().upper()
    print("----- INVIO FLAG", flgs, "A", destination, ", PORTA", port, "-----")
    res = scapy.sr(scapy.IP(dst=destination)/scapy.TCP(dport=port,flags=flgs), timeout=4) # Invio segmento TCP con flag richiesti attivi
    print("--- RISULTATI: ---")
    for r in res:
        r.show()
    print()

scelta = 1
while scelta != 0:
    print("-------------------- MENU: --------------------")
    print("1 - Invia pacchetto ICMP")
    print("2 - Invia segmento TCP SYN")
    print("3 - Invia segmento TCP con flag a scelta")
    print("0 - Chiudi il programma")
    print("\nDigitare il numero della scelta desiderata\n>", end=" ")
    scelta = int(input())
    match scelta:
        case 1:
            print("Host destinatario:", end=" ")
            dest = input()
            send_ping(dest)
        case 2:
            print("Host destinatario:", end=" ")
            dest = input()
            print("Porta destinatario:", end=" ")
            dest_port = int(input())
            send_tcp_syn(dest, dest_port)
        case 3:
            print("Host destinatario:", end=" ")
            dest = input()
            print("Porta destinatario:", end=" ")
            dest_port = int(input())
            send_tcp_flags(dest, dest_port)