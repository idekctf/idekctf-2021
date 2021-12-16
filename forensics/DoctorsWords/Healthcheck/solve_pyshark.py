import pyshark
from Crypto.Cipher import AES

file_name = '../Challenge/capture.pcapng'
cap = pyshark.FileCapture(file_name)

key = ''
ciphertext = ''
for packet in cap:
    # print(packet)
    if 'udp' not in packet or packet.udp.dstport.hex_value != 8080:
        continue
    # print(packet.udp.dstport.hex_value)
    # print(packet.udp._all_fields)
    key += packet.ip.ttl.main_field.raw_value
    ciphertext += packet.udp.payload.main_field.raw_value

print(f"Key: {key}")
print(f"Ciphertext: {ciphertext}")

key = bytes.fromhex(key)
ciphertext = bytes.fromhex(ciphertext)

nonce, tag, text = ciphertext[0:16], ciphertext[16:32], ciphertext[32:]

# let's assume that the key is somehow available again
cipher = AES.new(key, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify(text, tag)
print(data)