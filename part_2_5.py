"""
Write some code to print the SHA256 hash of the string "This is a string"
"""
from hashlib import sha256

s = "This is a string"

# Your code goes here
hashedWord = sha256(s.encode('utf-8')).hexdigest()
print(hashedWord)
