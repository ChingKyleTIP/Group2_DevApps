import tkinter as tk
from tkinter import simpledialog
import socket

def get_current_ip():
    # Get the current IPv4 address of the machine
    current_ip = socket.gethostbyname(socket.gethostname())
    ip_label.config(text="Current IPv4 address: " + current_ip)

def change_ip():
    # Prompt the user to enter a new IPv4 address
    new_ip = simpledialog.askstring("Change IPv4 Address", "Enter the new IPv4 address:")
    if new_ip:
        ip_label.config(text="New IPv4 address: " + new_ip)

def get_ipv6_address():
    # Get the current IPv6 address of the machine
    ipv6_addresses = [addrinfo[4][0] for addrinfo in socket.getaddrinfo(socket.gethostname(), None) if addrinfo[0] == socket.AF_INET6]
    if ipv6_addresses:
        ipv6_address = ipv6_addresses[0]  # Only display the first IPv6 address if multiple exist
        ipv6_label.config(text="Current IPv6 address: " + ipv6_address)
    else:
        ipv6_label.config(text="No IPv6 address found")

def change_ipv6_address():
    # Prompt the user to enter a new IPv6 address
    new_ipv6 = simpledialog.askstring("Change IPv6 Address", "Enter the new IPv6 address:")
    if new_ipv6:
        ipv6_label.config(text="New IPv6 address: " + new_ipv6)

# Create the main window
root = tk.Tk()
root.title("IP Address Management")

# Create a label to display IPv4 addresses
ip_label = tk.Label(root, text="")
ip_label.pack(pady=10)

# Create buttons to show current IPv4 and change IPv4
get_ip_button = tk.Button(root, text="Show Current IPv4", command=get_current_ip)
get_ip_button.pack()

change_ip_button = tk.Button(root, text="Change IPv4 Address", command=change_ip)
change_ip_button.pack()

# Create a label to display IPv6 addresses
ipv6_label = tk.Label(root, text="")
ipv6_label.pack(pady=10)

# Create buttons to show current IPv6 and change IPv6
get_ipv6_button = tk.Button(root, text="Show Current IPv6", command=get_ipv6_address)
get_ipv6_button.pack()

change_ipv6_button = tk.Button(root, text="Change IPv6 Address", command=change_ipv6_address)
change_ipv6_button.pack()

# Run the Tkinter event loop
root.mainloop()
