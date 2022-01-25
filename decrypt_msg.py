import base64

msg = 'GUYRFAhNCBIbSk9PRE4GHAcAFkZHDkoCBwEDEAUOFAtFQVhBTEseFQ0IAhAATk1ORQQEBwRcGRJP TVVVQwAPDRAEBggJQghGRE1IFAcBCAsUBA8EBVpKQVJNSAAKBQ4NCQQGRkcOShMJDw0cEBpGTlhB RRIKSAhGRE1IEwsGRk5YQUUWAkBMRhU='
key = 'babak.mahmoudian'

res = []
for i, c in enumerate(base64.b64decode(msg)):
    res.append(chr(ord(c) ^ ord(key[i % len(key)])))

print(''.join(res))
