
import random
import string
import secrets
import hashlib


#Generates a random letter, either upper or lower case
def GeneratedRandomLetter ():
    return random.choice(string.ascii_letters)

#Generates a random number, between 0-9
def GeneratedRandomNumber ():
    return random.choice(string.digits)

#Generates a symbol, example ! € % & @
def GeneratedRandomSymbol ():
    return random.choice(string.punctuation)

#Adds some salt for extra protection
def SaltGenerator (password):

    salt = secrets.token_hex(16)
    salted_output = salt + password

    hash_object = hashlib.sha256(salted_output.encode())
    hashed_text = hash_object.hexdigest()

    return hashed_text, salt


#Generates a randomized password after provided parameter lenght
def GeneratePassword (passwordLenght = 20):
    password = ""
    choices = [1, 2, 3]

    for i in range(passwordLenght):
        nextChar = random.choice(choices)

        if nextChar == 1: password += GeneratedRandomSymbol()
        elif nextChar == 2: password += GeneratedRandomNumber()
        else: password += GeneratedRandomLetter()

    print(password)
    return password


SaltGenerator(GeneratePassword())
