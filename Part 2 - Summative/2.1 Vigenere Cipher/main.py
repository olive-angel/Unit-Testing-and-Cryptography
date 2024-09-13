# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def vig_encode(text, keyword):
  """
  takes each index of both words and add them to select an index of the alphabet to return an encoded word
  """
  encodedWord = ""
  for i in range(len(text)):
    encodedWord = encodedWord + alpha[(alpha.find(text[i]) + alpha.find(keyword[i % len(keyword)])) % 26]
  return encodedWord

def vig_decode(text, keyword):
  """
  takes the index of both words and subtracts them to select an index of the alphabet to return a decoded word
  """
  decodedWord = ""
  for i in range(len(text)):
    decodedWord = decodedWord + alpha[(alpha.find(text[i]) - alpha.find(keyword[i % len(keyword)])) % 26]
  return decodedWord


test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
vig_key = "TEST"
enc = vig_encode(test, vig_key)
dec = vig_decode(enc, vig_key)
print(enc)
print(dec)
# If this worked, dec should be the same as test!