# Doctor's Words
**Category:** Misc/Forensics
**Difficulty:** Easy
**Author:** Louis#9459

## Description

The famous Dr. A. E. S., told me that my expected time to live is not very long. Can you decrypt the fragmented message he
sEnt me? He also left me A miXed footnote on my last CT scan result: 16 + 16 + CT.

## Distribution

- downloadable `capture.pcapng`

## Deploy notes

N/A

## Solution

Locate the relevant packets in the pcap (UDP packets to port 8080 from localhost), and write a script to parse those packets.
Concatenate the TTL of each packet to form the encryption key, and concatenate the UDP payload to form the ciphertext. Decrypt
the ciphertext using AES-EAX (16 bytes nonce, 16 bytes tag, rest ciphertext).