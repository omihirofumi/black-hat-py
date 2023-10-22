import socket

target_host = "127.0.0.1"
target_port = 9997

# create socket obj
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send
client.sendto(b"AABBCCDD", (target_host, target_port))

# recv
data, address = client.recvfrom(4096)

print(data.decode('utf-8'))
print(address)

client.close()