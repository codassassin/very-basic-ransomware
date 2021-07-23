from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP


with open('EMAIL_ME.txt', 'rb') as f:
    encFernetKey = f.read()
    print(encFernetKey)

# Private RSA key
private_key = RSA.importKey(open('private.pem').read())

# Private decrypter
privateCrypter = PKCS1_OAEP.new(private_key)

# Decrypted session key
decFernetKey = privateCrypter.decrypt(encFernetKey)
with open('PUT_ME_ON_DESKTOP.txt', 'wb') as f:
    f.write(decFernetKey)

print(f'[+] Private key: {private_key}')
print(f'[+] Private decrypter: {privateCrypter}')
print(f'[+] Decrypted Fernet key: {decFernetKey}')
print('[+] Decryption Completed')
