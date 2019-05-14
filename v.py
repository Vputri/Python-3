import binascii

encoded = binascii.unhexlify('HykgLSEtOGBsJSIlbCogLSsiNS1sdmwELS8nCik/ODcnKTglJy0TPi0rORMoLSITKy0gLTkTLj45OCkTKiM+LykTLSYtMUY=')
for xor_key in range(256):
    decoded = ''.join(chr(b ^ xor_key) for b in encoded)
    if decoded.isprintable():
        print(xor_key, decoded)
