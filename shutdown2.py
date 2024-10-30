import socket
import platform
import psutil
import tkinter as tk
from datetime import datetime

def get_system_info():
    info = {}
    info['Local Time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    info['PC Name'] = platform.node()
    info['IP Address'] = socket.gethostbyname(socket.gethostname())
    
    # Get network information
    interfaces = psutil.net_if_addrs()
    wifi_name = None
    ethernet_address = None
    
    for interface, addrs in interfaces.items():
        for addr in addrs:
            if addr.family == socket.AF_INET:
                if 'Wi-Fi' in interface or 'wlan' in interface.lower():
                    wifi_name = interface
                elif 'Ethernet' in interface or 'eth' in interface.lower():
                    ethernet_address = addr.address
    
    info['WiFi Name'] = wifi_name if wifi_name else 'Not connected to WiFi'
    info['Ethernet Address'] = ethernet_address if ethernet_address else 'Not connected to Ethernet'
    
    return info

def display_info():
    info = get_system_info()
    for key, value in info.items():
        label = tk.Label(root, text=f"{key}: {value}")
        label.pack()

root = tk.Tk()
root.title("System Information")
display_info()
root.mainloop()
