# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def caesar_encode(text, n):
    """
    returns string with letters shifted forward by n
    """
    alphabet = alpha*2
    encodedWord = ""
    for i in range(len(text)):
        for j in range(len(alpha)):
            if text[i] == alpha[j]:
                encodedWord = encodedWord + alphabet[j+n]
    return encodedWord


def caesar_decode(text, n):
    """
    returns string with letters shifted backward by n
    """
    alphabet = alpha*2
    decodedWord = ""
    for i in range(len(text)):
        for j in range(len(alpha)):
            if text[i] == alpha[j]:
                decodedWord = decodedWord + alphabet[(j+26) - n]
    return decodedWord


test = "HELLOWORLD"
shift = 5
enc = caesar_encode(test, shift)
dec = caesar_decode(enc, shift)
print(enc)
print(dec)
# If this worked, dec should be the same as test!
