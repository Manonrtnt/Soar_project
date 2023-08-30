## capture_helper.py
#from scapy.all import sniff
#
#captured_packets = []
#
#try:
#  # Capture de 10 paquets
#  packets = sniff(count=1)
#  captured_packets = [packet.summary() for packet in packets]
#except Exception as e:
#  captured_packets = [f"Erreur : {e}"]
#
#print(f"Captured packets: {captured_packets}")  

# capture_option1_paquet.py
#from scapy.all import sniff
#
#try:
#    # Capture de 1 paquet
#    packets = sniff(count=10)
#    captured_packets = [packet.summary() for packet in packets]
#
#    # Enregistrement des paquets dans un fichier
#    with open('captured_packets_option1.txt', 'w') as file:
#        for packet in captured_packets:
#            file.write(packet + '\n')
#
#except Exception as e:
#    captured_packets = [f"Erreur : {e}"]
#
#print(f"Captured packets (Option 1): {captured_packets}")


# capture_option1_paquet.py
from scapy.all import sniff

# Chemin du fichier de capture
file_path = '/home/osboxes/soar_project/capture/captured_packets_option1.txt'

try:
    # Capture de 1 paquet
    packets = sniff(count=10)
    captured_packets = [packet.summary() for packet in packets]
    
    # Écriture des paquets capturés dans le fichier
    with open(file_path, 'w') as file:
        for packet_summary in captured_packets:
            file.write(packet_summary + '\n')
    
except Exception as e:
    captured_packets = [f"Erreur : {e}"]

print(f"Captured packets (Option 1): {captured_packets}")