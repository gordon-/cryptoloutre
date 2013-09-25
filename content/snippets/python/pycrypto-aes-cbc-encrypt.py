from Crypto.Cipher import AES
from Crypto.Hash   import HMAC, SHA256
from Crypto        import Random


# the data must be padded to the block size (PKCS5 padding here)
pad = lambda s: s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)

plaintext = 'your secret message here'

encoded = pad(plaintext.encode('UTF-8'))

rnd = Random.new()
# To generate an AES-256 key
key     = rnd.read(32)

# To generate an AES-192 key
# key = rnd.read(24)

# To generate an AES-128 key
# key = rnd.read(16)

mac_key = rnd.read(32)

iv     = rnd.read(AES.block_size)
cipher = AES.new(key, AES.MODE_CBC, iv)
msg    = iv + cipher.encrypt(encoded)

# the MAC covers the whole encrypted message with IV
mac = HMAC.new(mac_key, msg, SHA256).digest()

result = (msg, mac)

print repr(result)
