from Crypto.Cipher import AES
from Crypto.Hash   import HMAC, SHA256


unpad = lambda s : s[0:-ord(s[-1])]

key, mac_key = # obtained from somewhere
msg, mac     = # obtained from somewhere

mac_verif    = HMAC.new(mac_key, msg, SHA256).digest()

def compare_mac(mac, verif):
    if len(mac) != len(mac_verif):
        print "invalid MAC size"
        return False

    result = 0
    # Constant time verification
    for x, y in zip(mac, mac_verif):
        result |= ord(x) ^ ord(y)

    return result == 0

if compare_mac(mac, mac_verif):
    iv         = msg[:16]
    ciphertext = msg[16:]

    cipher     = AES.new(key, AES.MODE_CBC, iv)
    bytes      = unpad(cipher.decrypt(ciphertext))

    print "message: "+encoded.decode('UTF-8')
