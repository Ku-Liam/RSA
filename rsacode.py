from math import gcd #greatest common divisor
import random

def generate_number1(phi_n): #for public key
    number1 = 2
    possiblenumber1 = [] #array is used because when e is generated multiple values are formed and we need to choose one of them
    while number1 < phi_n: #check for each possible number of e where e is less than phi_n and the greatest common divisor is equal to 1
        commondivisor = gcd(number1, phi_n)
        if commondivisor == 1:
            possiblenumber1.append(number1) #numbers that fufill requirements are added to the array
        number1 = number1 + 1
    number1 = random.choice(possiblenumber1) #when all numbers are added to array, random number is from the array is chosen
    return number1  #this number has to be random to ensure security

def generate_number2(number1, phi_n): #for private key
    number2 = 1 
    number3 = (number2*number1)%phi_n #modulus of number 1 x number 2 by phi_n has a result of 1 
    while number3 != 1:
        number2 = number2+1
        number3 = (number2*number1)%phi_n
    return number2

def encrypt(message, key): #message and public key are sent to this function
    words = message.split(" ")
    cipher = ""
    cipher_texts = [] #each message is split into words. words will be added to the array 
    for i in words: #each word in the message is going to be split into letters
        word = encrypt_word(i, key) #letters are encrypted using public key
        cipher_texts.append(word)
    for j in cipher_texts:
        cipher = cipher + str(j) + " "
        print(cipher)
    return cipher

def encrypt_word(word, key):
    encrypted_values = []
    values =[]
    n, e = key
    cipher = ""
    for i in word:
        x = ord(i)
        values.append(x)
    for j in values:
        c = (j ** e) % n
        encrypted_values.append(c)
    for k in encrypted_values:
        cipher = cipher + str(k) + " "
    return cipher

def decrypt(message, key): #receiving the encrypted text
    numbers = message.split(" ")
    original = ""
    decryption = []
    for i in numbers:
        pal = decrypt_number(i, key)
        decryption.append(pal)
    for j in decryption:
        original = original + str(j) + (" ")
    return original

def decrypt_number(number, key):
    list_numbers_decrypted = []
    list_numbers = []
    n, d = key
    decrypted=""
    numbers = number.split(" ")
    for i in numbers:
        if(i != ''):
            x = int(i)
            list_numbers.append(x)
    for j in list_numbers:
        m = (j ** d) % n
        list_numbers_decrypted.append(m)
    for k in list_numbers_decrypted:
        letter = chr(k)
        decrypted = decrypted + str(letter)
    return decrypted

def generate_keys():
    prime1 = 239 #two large prime numbers, for more complexity of calculations and secure encryption
    prime2 = 103
    n = prime2 * prime1 #product of the two prime numbers 
    phi_n = (prime2 - 1) * (prime1 - 1)
    #phi_n is the phi of n which is the euler's totient function where 
    #If we know some number N is the product of two primes, P one and P two
    #then phi of N is just the value of phi for each prime multiplied together
    #or P one minus one, times P two minus one.

    e = generate_number1(phi_n) #phi_n is passed to form e and d
    d = generate_number2(e, phi_n)
    return (n, e), (n, d) 



public_key, private_key = generate_keys()
message = input("Message: ")
encrypt_message = encrypt(message, public_key)

print("decrypt: "+ str(encrypt_message))
#number one to the power of number two
decrypted_message = decrypt(encrypt_message, private_key)

print(str(decrypted_message))


#rsa needs public and private key. public key encrypts and each user has a private key that can decrypt the message
#each time a message is passed each letter has its own ascii value. this ascii value is the one we are encrypting.
#so we need to 
   