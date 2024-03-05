import tkinter as tk
import socket
import ipaddress

def get_current_ip():
    # Get the current IPv4 address and subnet mask of the machine
    ipv4_address = socket.gethostbyname(socket.gethostname())
    ipv4_subnet_mask = socket.inet_ntoa(socket.inet_aton('255.255.255.0'))
    
    # Determine the IP class
    first_octet = int(ipv4_address.split('.')[0])
    if 1 <= first_octet <= 126:
        ipv4_class = 'A'
    elif 128 <= first_octet <= 191:
        ipv4_class = 'B'
    elif 192 <= first_octet <= 223:
        ipv4_class = 'C'
    elif 224 <= first_octet <= 239:
        ipv4_class = 'D (Multicast)'
    elif 240 <= first_octet <= 255:
        ipv4_class = 'E (Reserved)'
    else:
        ipv4_class = 'Unknown'

    # Display IPv4 information with breaks
    ipv4_info = "Current IPv4 address: " + ipv4_address + "\n(IPv4), Subnet Mask: " + ipv4_subnet_mask + "\nClass: " + ipv4_class
    ipv4_label.config(text=ipv4_info)

def get_ipv6_address():
    # Get the current IPv6 address of the machine
    ipv6_addresses = [addrinfo[4][0] for addrinfo in socket.getaddrinfo(socket.gethostname(), None) if addrinfo[0] == socket.AF_INET6]
    if ipv6_addresses:
        ipv6_address = ipv6_addresses[0]  # Only display the first IPv6 address if multiple exist
        ipv6_subnet_mask = ipaddress.IPv6Network(ipv6_address).netmask

        # Display IPv6 information with breaks
        ipv6_info = "Current IPv6 address: " + ipv6_address + "\n(IPv6), Subnet Mask: " + str(ipv6_subnet_mask)
        ipv6_label.config(text=ipv6_info)
    else:
        ipv6_label.config(text="No IPv6 address found")

# Create the main window
root = tk.Tk()
root.title("IP Address Viewer")

# Create a label to display IPv4 addresses
ipv4_label = tk.Label(root, text="")
ipv4_label.pack(pady=10)

# Create buttons to show current IPv4
get_ipv4_button = tk.Button(root, text="Show Current IPv4", command=get_current_ip)
get_ipv4_button.pack()

# Create a label to display IPv6 addresses
ipv6_label = tk.Label(root, text="")
ipv6_label.pack(pady=10)

# Create buttons to show current IPv6
get_ipv6_button = tk.Button(root, text="Show Current IPv6", command=get_ipv6_address)
get_ipv6_button.pack()

# Run the Tkinter event loop
root.mainloop()
