"""
USE AT YOUR OWN RISK. 
THE USE OF THIS SCRIPT IS ONLY FOR EDUCATION PURPOSES ONLY.
USE THIS SCRIPT ONLY WITH PERMISSION FROM THE OWNER OF THE IP ADDRESS YOU ARE TRYING TO SCAN.
BEWARE THAT YOU MAYBE NEED THE PERMISSION OF YOUR ISP.
"""

from concurrent.futures import thread
import socket
import threading
from queue import Queue

target = input("Enter an IP adress: ")
queue = Queue()
open_ports = []

def PortScanner(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False

def fill_queue(ports):
    for port in ports:
        queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        if PortScanner(port):
            print("Port {} is open".format(port))
            open_ports.append(port)

port_list = range(1, 65536)
fill_queue(port_list)

thread_list = []

for t in range(500):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print("Open ports: ", open_ports)
