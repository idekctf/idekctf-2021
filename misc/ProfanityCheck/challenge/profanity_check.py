#!/usr/bin/env python3

from unicodedata import normalize
import random

i = input(">>> ")

for n in range(10000):
  if random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") in i:
    print("Profanity detected. Exiting.")
    exit(0)

i = normalize("NFC", i)

blacklist = ["__", "()", "{", "}", "[", "]", ";", ":", "!", "@", "#", "$", "%", "^", "&", "*", ",", "class", "mro", "sub", "glob"]

for n in blacklist:
  if n in i:
    print("Profanity detected. Exiting.")
    exit(0)

eval(i)
