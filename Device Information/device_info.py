import socket
import psutil
host_name = socket.gethostname()
ip_address= socket.gethostbyname(host_name)
memory_info = psutil.virtual_memory()
disk_info = psutil.disk_usage("/")

print("Host name :", host_name)
#print("IP Address :", ip_address)
print("Memory information :", memory_info)
print("Disk information :", disk_info)