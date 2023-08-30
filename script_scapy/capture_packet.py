# capture_helper.py
from scapy.all import sniff

def capture_packets(choice):
    captured_packets = []

    if choice == 'Option 1 : Capturer tous les paquets':
        try:
            # Capture de 10 paquets
            packets = sniff(count=1)
            captured_packets = [packet.summary() for packet in packets]
        except Exception as e:
            captured_packets = [f"Erreur : {e}"]
    elif choice == 'Option 2 : Capturer les paquets de la couche Ethernet':
        try:
            # Capture des paquets de la couche Ethernet
            packets = sniff(count=10, filter="ether")
            captured_packets = [packet.summary() for packet in packets]
        except Exception as e:
            captured_packets = [f"Erreur : {e}"]
    elif choice == 'Option 3 : Capturer les paquets de la couche IP':
        try:
            # Capture des paquets de la couche IP
            packets = sniff(count=10, filter="ip")
            captured_packets = [packet.summary() for packet in packets]
        except Exception as e:
            captured_packets = [f"Erreur : {e}"]
    elif choice == 'Option 4 : Capturer les paquets de la couche TCP':
        try:
            # Capture des paquets de la couche TCP
            packets = sniff(count=10, filter="tcp")
            captured_packets = [packet.summary() for packet in packets]
        except Exception as e:
            captured_packets = [f"Erreur : {e}"]

    print(f"Captured packets: {captured_packets}")  
    return captured_packets






