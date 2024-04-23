#try
import tkinter as tk
from tkinter import simpledialog
import socket

def get_current_ip():
    current_ip = socket.gethostbyname(socket.gethostname())
    ip_label.config(text="Current IPv4 address: " + current_ip)

def change_ip():
    new_ip = simpledialog.askstring("Change IPv4 Address", "Enter the new IPv4 address:")
    if new_ip:
        ip_label.config(text="New IPv4 address: " + new_ip)

def get_ipv6_address():
    ipv6_addresses = [addrinfo[4][0] for addrinfo in socket.getaddrinfo(socket.gethostname(), None) if addrinfo[0] == socket.AF_INET6]
    if ipv6_addresses:
        ipv6_address = ipv6_addresses[0]
        ipv6_label.config(text="Current IPv6 address: " + ipv6_address)
    else:
        ipv6_label.config(text="No IPv6 address found")

def change_ipv6_address():
    new_ipv6 = simpledialog.askstring("Change IPv6 Address", "Enter the new IPv6 address:")
    if new_ipv6:
        ipv6_label.config(text="New IPv6 address: " + new_ipv6)


root = tk.Tk()
root.title("IP Address Management")

ip_label = tk.Label(root, text="")
ip_label.pack(pady=10)

get_ip_button = tk.Button(root, text="Show Current IPv4", command=get_current_ip)
get_ip_button.pack()

change_ip_button = tk.Button(root, text="Change IPv4 Address", command=change_ip)
change_ip_button.pack()

ipv6_label = tk.Label(root, text="")
ipv6_label.pack(pady=10)

get_ipv6_button = tk.Button(root, text="Show Current IPv6", command=get_ipv6_address)
get_ipv6_button.pack()

change_ipv6_button = tk.Button(root, text="Change IPv6 Address", command=change_ipv6_address)
change_ipv6_button.pack()

root.mainloop()
