# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def sub_encode(text, codebet):
    """
    take user text and alphabet to return an encoded word
    """
    encodedWord = ""
    text = text.upper()
    codebet = codebet.upper()
    for i in range(len(text)):
        for j in range(len(alpha)):
            if text[i] == alpha[j]:
                encodedWord = encodedWord + codebet[j]
    return encodedWord


def sub_decode(text, codebet):
    """
    take user text and alphabet to return a decoded word
    """
    decodedWord = ""
    text = text.upper()
    codebet = codebet.upper()
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
