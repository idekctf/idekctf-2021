import hashlib
output = "9ee2275f8699c3146b65fabc390d83df5657a96c39ab58933f82d39b"
def recursion(string, length):
	if len(string) == length:
		hashresult = hashlib.md5(bytes(string, 'utf-8')).digest()
		sha1 = hashlib.sha1(hashresult)
		sha224 = hashlib.sha224(sha1.digest())
		for i in range(0, 10):
			sha1 = hashlib.sha1(sha224.digest())
			sha224 = hashlib.sha224(sha1.digest())
		output2 = sha224.hexdigest()
		if output2 == output:
			print(string)
			return
		return
	for i in range(65, 123):
		recursion(string + chr(i), length)
recursion("", 4)
