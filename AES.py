from Crypto.Cipher import AES

# cipher = AES.new(key, AES.MODE_CBC, IV)

key = bytes.fromhex("36f18357be4dbd77f050515c73fcf9f2")

cipherText = "69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329"

IV = bytes.fromhex(cipherText[:32])
text = bytes.fromhex(cipherText[32:])

# if you want to encrypt a message - Change decrypt to encrypt(message)
# ***************************
# Decrypting a CBC

cipher = AES.new(key, AES.MODE_CBC, IV)
print(cipher.decrypt(text))


# ***************************
# Decrypting a CTR

final = ""
x = 32
counter = 0
nounce = cipherText[:16]

while x <= len(cipherText):
    # original number always the same
    number = int(cipherText[16:32], 16)
    number += counter

    IV = bytes.fromhex(nounce + str(hex(number))[2:])
    message = bytes.fromhex(cipherText[x: x + 32])

    cipher = AES.new(key, AES.MODE_CTR, counter=lambda: IV)
    temp = str(cipher.decrypt(message))
    temp = temp[2: len(temp) - 1]
    final = final + temp
    counter += 1
    x += 32

print(final)
