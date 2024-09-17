import math

# Read the instructions to see what to do!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# PART 1
# These functions are provided for you!
def mod_inverse_helper(a, b):
    q, r = a//b, a%b
    if r == 1:
        return (1, -1 * q)
    u, v = mod_inverse_helper(b, r)
    return (v, -1 * q * v + u)

def mod_inverse(a, m):
    assert math.gcd(a, m) == 1, "You're trying to invert " + str(a) + " in mod " + str(m) + " and that doesn't work!"
    return mod_inverse_helper(m, a)[1] % m


# These are the functions you'll need to write:
def affine_encode(text, a, b):
    """
    use affine method to return encoded text
    """
    print(text)
    encodedWord = ""
    for i in range(len(text)):
        j = alpha.index(text[i])
        encodedWord = encodedWord + alpha[(a*j+b) % 26]
    return encodedWord

def affine_decode(text, a, b):
    decodedWord = ""
    for i in range(len(text)):
        j= alpha.index(text[i])
        decodedWord = decodedWord + alpha[((j-b) % 26 *mod_inverse(a, 26)) % 26]
    return decodedWord

test = "HELLOWORLD"
a = 3
b = 9
enc = affine_encode(test, a, b)
dec = affine_decode(enc, a, b)
print(enc)
print(dec)
# If this worked, dec should be the same as test!



# PART 2
# These  are the functions you'll need to write:
def convert_to_num(ngram):
    """
    sum of multipied powered index of increasing powers of 26 by alphabet index of each letter
    returns a large number gram
    """
    num = 0
    for i in range(len(ngram)):
        num = num + 26**i*alpha.index(ngram[i])
    return num

def convert_to_text(num, n):
    """
    divide large number gram by taking the remainder of each divisor
    returns text
    """
    text = ""
    for i in range(n):
        text = text + alpha[num % 26]
        num = num // 26
    return text

test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
l = len(test)
num = convert_to_num(test)
answer = convert_to_text(num, l)
print(num)
print(answer)
# If this worked, answer should be the same as test!



# PART 3

# These are the functions you'll need to write:
def affine_n_encode(text, n, a, b):
    """

    """

    x = convert_to_num(text)
    newText =

#def affine_n_decode(text, n, a, b):
    #return ''

test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
n = 5
a = 347
b = 1721
#enc = affine_n_encode(test, n, a, b)
#dec = affine_n_decode(enc, n, a, b)
#print(enc, dec)
# If this worked, dec should be the same as test!