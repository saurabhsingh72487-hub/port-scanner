from port_scanner import get_open_ports

print("Scanning...")
print(get_open_ports("scanme.nmap.org", [20, 25], True))
print("Done")