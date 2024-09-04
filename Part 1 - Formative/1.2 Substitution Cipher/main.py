# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def sub_encode(text, codebet):
    encodedWord = ""
    for i in range(len(text)):
        for j in range(len(alpha)):
            if text[i] == alpha[j]:
                encodedWord = encodedWord + codebet[j]
    return encodedWord


def sub_decode(text, codebet):
    decodedWord = ""
    for i in range (len(text)):
        for j in range(len(codebet)):
            if text[i] == codebet[j]:
                decodedWord = decodedWord + alpha[j]
    return decodedWord


test = "HELLOWORLD"
cipher_alphabet = "WJKUXVBMIYDTPLHZGONCRSAEFQ"
enc = sub_encode(test, cipher_alphabet)
dec = sub_decode(enc, cipher_alphabet)
print(enc)
print(dec)
# If this worked, dec should be the same as test!
