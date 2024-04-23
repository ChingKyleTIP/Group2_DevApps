#try
import tkinter as tk
import socket

def get_current_ip():

    current_ip = socket.gethostbyname(socket.gethostname())
    ip_label.config(text="Current IPv4 address: " + current_ip)

def get_ipv6_address():
    ipv6_addresses = [addrinfo[4][0] for addrinfo in socket.getaddrinfo(socket.gethostname(), None) if addrinfo[0] == socket.AF_INET6]
    if ipv6_addresses:
        ipv6_address = ipv6_addresses[0]
        ipv6_label.config(text="Current IPv6 address: " + ipv6_address)
    else:
        ipv6_label.config(text="No IPv6 address found")
root = tk.Tk()
root.title("IP Address Viewer")
ip_label = tk.Label(root, text="")
ip_label.pack(pady=10)
get_ip_button = tk.Button(root, text="Show Current IPv4", command=get_current_ip)
get_ip_button.pack()
ipv6_label = tk.Label(root, text="")
ipv6_label.pack(pady=10)
get_ipv6_button = tk.Button(root, text="Show Current IPv6", command=get_ipv6_address)
get_ipv6_button.pack()
root.mainloop()
