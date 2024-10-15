from scapy.all import sendp

sendp("I’m travelling on Ethernet", iface="enp2s0", loop=1, inter=0.2)
