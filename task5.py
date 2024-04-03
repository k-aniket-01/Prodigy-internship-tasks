import sys
from scapy.all import *

def packet_callback(packet):
    if packet.haslayer(TCP):
        source_ip = packet[IP].src
        dest_ip = packet[IP].dst
        protocol = packet[IP].proto

        payload = str(packet[TCP].payload)

        # Print captured packet information
        print(f"Source IP: {source_ip}")
        print(f"Destination IP: {dest_ip}")
        print(f"Protocol: {protocol}")
        print(f"Payload: {payload}\n")

def main():
    if len(sys.argv) < 2:
        print("Usage: python packet_sniffer.py <interface>")
        exit(1)

    interface = sys.argv[1]

    try:
        sniff(filter="tcp", prn=packet_callback, store=0, iface=interface)
    except KeyboardInterrupt:
        print("Packet sniffer stopped.")

if __name__ == "__main__":
    main()