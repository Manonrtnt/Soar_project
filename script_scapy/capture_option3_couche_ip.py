# capture_option3_couche_ip.py
from scapy.all import sniff

try:
    # Capture des paquets de la couche IP
    packets = sniff(count=10, filter="ip")
    captured_packets = [packet.summary() for packet in packets]
except Exception as e:
    captured_packets = [f"Erreur : {e}"]

print(f"Captured packets (Option 3): {captured_packets}")

# Écrire les paquets capturés dans un fichier
with open('/home/osboxes/soar_project/capture/capture_option3.txt', 'w') as file:
    for packet in captured_packets:
        file.write(packet + '\n')

print(f"Fichier 'capture_option3.txt' mis à jour")