import socket
from common_ports import ports_and_services


def get_open_ports(target, port_range, verbose=False):
    open_ports = []

    try:
        ip_address = socket.gethostbyname(target)
    except socket.gaierror:
        if target.replace(".", "").isdigit():
            return "Error: Invalid IP address"
        return "Error: Invalid hostname"

    for port in range(port_range[0], port_range[1] + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((ip_address, port))

        if result == 0:
            open_ports.append(port)

        sock.close()

    if verbose:
        try:
            hostname = socket.gethostbyaddr(ip_address)[0]
        except socket.herror:
            hostname = target

        output = f"Open ports for {hostname} ({ip_address})\n"
        output += "PORT     SERVICE\n"

        for port in open_ports:
            service = ports_and_services.get(port, "")
            output += f"{port:<9}{service}\n"

        return output.rstrip()

    return open_ports