import hashlib

password = input('Password:')
m = hashlib.sha256()
m.update(password.encode('utf-8'))
hash = m.digest()
print(hash) # b'\xda$\x8e\xea\xff\xa5s\xda\x8c2<>\xb5j\xaf2\xecl\xe2D\xe4\x01\xa2LU\xf3\x0c\x90}\x0b\xbf\xb5'
print(type(hash)) # <class 'bytes'>