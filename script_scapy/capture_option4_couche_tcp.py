# capture_option4_couche_tcp.py
from scapy.all import sniff

try:
    # Capture des paquets de la couche TCP
    packets = sniff(count=10, filter="tcp")
    captured_packets = [packet.summary() for packet in packets]
except Exception as e:
    captured_packets = [f"Erreur : {e}"]

print(f"Captured packets (Option 4): {captured_packets}")

# Écrire les paquets capturés dans un fichier
with open('/home/osboxes/soar_project/capture/capture_option4.txt', 'w') as file:
    for packet in captured_packets:
        file.write(packet + '\n')

print(f"Fichier 'capture_option4.txt' mis à jour")