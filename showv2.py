import tkinter as tk
from tkinter import simpledialog
import socket
import ipaddress
import requests
import psutil
from PIL import Image, ImageTk
import geocoder

# Google Maps Geocoding API key
API_KEY = "AIzaSyAxCMaK-7N1SwNX2WiKhrH6acZyBi8fxMQ"

def print_network_interfaces():
    for interface, addrs in psutil.net_if_addrs().items():
        print(f"Interface: {interface}")
        for addr in addrs:
            print(f"- Address: {addr.address}")
            print(f"  Family: {addr.family}")
            print(f"  Broadcast: {addr.broadcast}")
            print(f"  Netmask: {addr.netmask}")
            print(f"  PTY: {addr.ptp}")
            print(f"  MAC: {addr.address}")
        print()

def get_current_ip(target_interface):
    try:
        ip_address = ""
        for interface, addrs in psutil.net_if_addrs().items():
            if interface == target_interface:
                for addr in addrs:
                    if addr.family == socket.AF_INET:
                        ip_address = addr.address
                        break
                if ip_address:
                    break
        
        if ip_address:
            ipv4_subnet_mask = socket.inet_ntoa(socket.inet_aton('255.255.255.0'))
            
            # Determine the IP class
            first_octet = int(ip_address.split('.')[0])
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
            ipv4_info = "Current IPv4 address: " + ip_address + "\n(IPv4), Subnet Mask: " + ipv4_subnet_mask + "\nClass: " + ipv4_class
            ipv4_label.config(text=ipv4_info)
        else:
            ipv4_label.config(text=f"No IPv4 address found for interface '{target_interface}'")
    except Exception as e:
        ipv4_label.config(text="Error: " + str(e))

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

def get_current_location():
    try:
        # Get current location using geocoder
        location = geocoder.ip('me')

        if location.ok:
            # Display location information
            if hasattr(location, 'region'):
                location_info = f"Your Current Location:\nLatitude: {location.lat}\nLongitude: {location.lng}\nCity: {location.city}\nRegion: {location.region}"
            else:
                location_info = f"Your Current Location:\nLatitude: {location.lat}\nLongitude: {location.lng}\nCity: {location.city}"
            geolocation_label.config(text=location_info)
        else:
            geolocation_label.config(text="Unable to retrieve current location")
    except Exception as e:
        geolocation_label.config(text="Error: " + str(e))

# Create the main window
root = tk.Tk()
root.title("IP Address Viewer")

try:
    # Open the image file
    img = Image.open("C:/Users/Ching/Documents/DevOps/V1.jpg")

    # Resize the image to fit the window size
    width, height = root.winfo_screenwidth(), root.winfo_screenheight()
    img = img.resize((width, height), Image.BILINEAR)

    # Convert the Image object to a Tkinter-compatible photo image
    background_image = ImageTk.PhotoImage(img)
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
except Exception as e:
    print("Error loading background image:", e)

# Create a label to display IPv4 addresses
ipv4_label = tk.Label(root, text="")
ipv4_label.pack(pady=10)

# Create buttons to show current IPv4
get_ipv4_button = tk.Button(root, text="Show Current IPv4", command=lambda: get_current_ip("Ethernet"))  # Change "Ethernet" to your network interface name
get_ipv4_button.pack()

# Create a label to display IPv6 addresses
ipv6_label = tk.Label(root, text="")
ipv6_label.pack(pady=10)

# Create buttons to show current IPv6
get_ipv6_button = tk.Button(root, text="Show Current IPv6", command=get_ipv6_address)
get_ipv6_button.pack()

# Create a label to display geolocation information
geolocation_label = tk.Label(root, text="")
geolocation_label.pack(pady=10)

# Button to fetch current location
get_current_location_button = tk.Button(root, text="Get Current Location", command=get_current_location)
get_current_location_button.pack()

# Run the Tkinter event loop
root.mainloop()
