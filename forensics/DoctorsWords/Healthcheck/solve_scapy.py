from scapy.all import *
from Crypto.Cipher import AES
from binascii import hexlify

key = b''
ciphertext = b''

scapy_cap = rdpcap('../Challenge/capture.pcapng')
for packet in scapy_cap:
    try:
        udp_layer = packet['UDP']
        if udp_layer.dport != 8080:
            continue
        key += int.to_bytes(packet['IP'].ttl, length=1, byteorder='big')
        ciphertext += raw(udp_layer.payload)
    except IndexError:
        continue

print(f"Key: {hexlify(key).decode('ascii')}")
print(f"Ciphertext: {hexlify(ciphertext).decode('ascii')}")

nonce, tag, text = ciphertext[0:16], ciphertext[16:32], ciphertext[32:]

cipher = AES.new(key, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify(text, tag)
print(data.decode('ascii'))