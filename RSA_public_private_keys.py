from Crypto.PublicKey import RSA


# Generates RSA Encryption + Decryption keys / Public + Private keys
key = RSA.generate(2048)

privateKey = key.export_key()
with open('private.pem', 'wb') as f:
    f.write(privateKey)

publicKey = key.publickey().export_key()
with open('public.pem', 'wb') as f:
    f.write(publicKey)
