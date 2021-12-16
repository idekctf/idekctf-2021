import string
import hashlib
import random
a = random.choice(string.ascii_letters)
b = random.choice(string.ascii_letters)
c = random.choice(string.ascii_letters)
d = random.choice(string.ascii_letters)
password2hash = b"WDOb"#a+b+c+d
hashresult = hashlib.md5(password2hash).digest()
sha1 = hashlib.sha1(hashresult)
sha224 = hashlib.sha224(sha1.digest())
for i in range(0, 10):
	sha1 = hashlib.sha1(sha224.digest())
	sha224 = hashlib.sha224(sha1.digest())
output = sha224.hexdigest()
print("output: " + output)