import argparse
import random
import math
import sys

'''
Classic Ciphers
ciphers.py
Python program that utilises five different cipher algorithms to encrypt/decrypt a given file.
The five ciphers are as follow:

Caesar cipher
Simple substitution cipher
Poly-alphabetic cipher
Transposition cipher
Atbash cipher

When encrypted/decrypted, the message gets outputted to a new text file.
Implementation assisted by the following references listed in the function headers.

Libaries used:
argparse: Argument parser for the command line
random: used in a variation of the substitution cipher to randomise key; serves as an option if user wants to use it
sys: used to quit program if errors arise
math: used for transposition cipher

@Author: Benny Fung
'''

#Initialize lowercase alphabet for convenience
global letters
letters = 'abcdefghijklmnopqrstuvwxyz'

'''
Argument parser for command line.
Utilizes flags to toggle options accordingly.
Example usage:
[python] [ciphers.py] [-e] [-f message.txt] [-c1] [-k 3] 
'''
def func():
	parser = argparse.ArgumentParser()
	parser.add_argument("-e", "--encrypt", help = "Encrypt", action = "store_true")
	parser.add_argument("-d", "--decrypt", help = "Decrypt", action = "store_true")
	parser.add_argument('-k', '--key', help = 'Key value (DEFAULT is 4 if not inputted')
	parser.add_argument('-c1', '--c1', help = 'Caesar cipher', action = "store_true")
	parser.add_argument('-c2', '--c2', help = 'Simple substitution cipher', action = "store_true")
	parser.add_argument('-c3', '--c3', help = 'Poly-alphabetic cipher', action = "store_true")
	parser.add_argument('-c4', '--c4', help = 'Transposition cipher', action = "store_true")
	parser.add_argument('-c5', '--c5', help = 'Atbash cipher', action = "store_true")
	parser.add_argument('-f', '--file', help = 'Takes in file', nargs = '?')
	return parser.parse_args()

'''
Caesar cipher is a mono-alphabetic cipher wherein each letter of the plaintext is substituted
by another letter to form the ciphertext. It is a simplest form of substitution cipher scheme.
This cryptosystem is generally referred to as the Shift Cipher. The concept is to replace each 
alphabet by another alphabet which is ‘shifted’ by some fixed number between 0 and 25.

References: 
https://www.tutorialspoint.com/cryptography/traditional_ciphers.htm
https://github.com/CryptoUSF/Course-Material/blob/master/references/books/1911%20-%20Manual%20of%20Cryptography.pdf
https://www.geeksforgeeks.org/caesar-cipher/

The following functions take in a message and key to perform encryption/decryption.

Example usage: 
[python] [ciphers.py] [-e] [-f message.txt] [-c1] [-k 3]
[python] [ciphers.py] [-d] [-f outputMessage.txt] [-c1] [-k 3]
'''
def encryptCaesar(msg, key):
	result = ""
	msg = msg.lower()
	for i in msg:
		char = (letters.index(i)+key)%26
		result+=letters[char]
	file = open("outputMessage.txt","w")
	file.write(result)
	file.close()
	print("Message outputted to file 'outputMessage.txt'")
	return result

def decryptCaesar(msg, key):
	result = ""
	msg = msg.lower()
	for i in msg:
		char = (letters.index(i)-key)%26
		result+=letters[char]
	file = open("outputMessage.txt","w")
	file.write(result)
	file.close()
	print("Message outputted to file 'outputMessage.txt'")
	return result

'''
Simple substitution cipher that replaces a letter with another letter in the alphabet. 
In this algorithm, letters are randomly shuffled and uniquely paired with another letter. Whitespaces are removed.

References: 

https://github.com/CryptoUSF/Course-Material/blob/master/references/books/1911%20-%20Manual%20of%20Cryptography.pdf
https://pycipher.readthedocs.io/en/master/#simple-substitution-cipher
http://www.practicalcryptography.com/ciphers/simple-substitution-cipher/
https://stackoverflow.com/questions/36188226/substitution-cipher-python

The following functions take in a message to perform encryption/decryption.

Example usage: 
[python] [ciphers.py] [-e] [-f message.txt] [-c2]
[python] [ciphers.py] [-d] [-f message.txt] [-c2]
'''
def encryptSimpleSubstitution(msg):
	msg = msg.lower()
	result = ""
	keyList = list(letters)
	random.shuffle(keyList)
	key = ''.join(keyList)
	for char in msg:
		if not (char.isspace()):
			if char in letters:
				result += key[letters.index(char)]
			else:
				result += char
	file = open("outputMessage.txt","w")
	file.write(result)
	file.close()
	print("key is: " + key)
	print("Message outputted to file 'outputMessage.txt'")
	return result

def decryptSimpleSubstitution(msg):
	key = input("Input 26 letter key: ").lower()	
	if not key.isalpha() or len(key) != 26:
		print("Error: please input 26 unique alphabetical char")
		sys.exit(0)
	msg = msg.lower()
	result = ""
	for char in msg:
		temp = char
		if not (char.isspace()):
			if char in letters:
				temp = letters[key.index(char)]
				result += temp
			else:
				result += char
	file = open("outputMessage.txt","w")
	file.write(result)
	file.close()
	print("key is: " + key)
	print("Message outputted to file 'outputMessage.txt'")
	return result
'''
Transposition ciphers, in which the words or letters remain the same, but their order is changed.
The order is determined by the key, which divides the message into a matrix. This is similar to the ZigZag cipher,
which transposes symbols in the plaintext by first writing the characters down the first column, then up the next column,
then down the third and so forth filling out a grid. The plaintext is made by reading
the grid rows left-to-right/top-to-bottom.

Concept and implementation from references:
https://inventwithpython.com/hacking/chapter9.html
https://www.tutorialspoint.com/cryptography/traditional_ciphers.htm
http://marshallfoundation.org/library/wp-content/uploads/sites/16/2014/09/WFFvol05watermark.pdf
https://github.com/CryptoUSF/Course-Material/blob/master/references/books/1911%20-%20Manual%20of%20Cryptography.pdf

The following functions take in a message and key to perform encryption/decryption.

Example usage: 
[python3] [ciphers.py] [-f plaintext.txt] [-c4] [-e] [-k 5]
[python3] [ciphers.py] [-f outputMessage.txt] [-c4] [-d] [-k 5]
'''

def transpositionEncrypt(msg, key):
	msg = msg.lower().replace(" ", "")
	result = ""
	grid = [""]*key
	for r in range(key):
		temp = r
		while temp < len(msg):
			grid[r] += msg[temp]
			temp += key
	result = ''.join(grid)
	file = open("outputMessage.txt","w")
	file.write(result)
	file.close()
	print("Message outputted to file 'outputMessage.txt'")
	return result

def transpositionDecrypt(msg, key):
	result = ""
	c = math.ceil(len(msg)/key)
	r = key
	size = (c*r)-len(msg)
	grid = [""]*int(c)
	row = 0
	col = 0
	for char in msg:
		grid[col]+=char
		col+=1
		if (col==c) or (col==c-1 and row>=r-size):
			col=0
			row+=1
	result = ''.join(grid)
	file = open("outputMessage.txt","w")
	file.write(result)
	file.close()
	print("Message outputted to file 'outputMessage.txt'")
	return result

'''
"Polyalphabetic Cipher is a substitution cipher in which the cipher alphabet
for the plain alphabet may be different at different places during the encryption process"

The following resembles closely to the Vigenere cipher, as it utilizes ASCII values for shifts.
The key is essential in determining the shifts in the plaintext.
"This scheme of cipher uses a text string (say, a word) as a key,
which is then used for doing a number of shifts on the plaintext.
Vigenere cipher"

Reference:
https://www.tutorialspoint.com/cryptography/traditional_ciphers.htm
http://crypto.interactive-maths.com/vigenegravere-cipher.html
https://github.com/CryptoUSF/Course-Material/blob/master/references/books/1911%20-%20Manual%20of%20Cryptography.pdf

The following functions take in a message to perform encryption/decryption.
Usage:
[python3] [ciphers.py] [-f outputMessage.txt] [-c3] [-e]
[python3] [ciphers.py] [-f outputMessage.txt] [-c3] [-d]
'''
def encryptPolyalphabetic(msg):
	msg = msg.lower().replace(" ", "") 
	key = str(input("Enter alphabetic key: "))
	if not key.isalpha():
		print("Error: must be alphabetic")
		sys.exit(1)
	result = ""
	index = 0
	val = 0 
	msgVal = 0
	temp = 0
	for i in msg:
		msgVal = ord(i)-97
		val = ord(key[index])-97
		temp = (msgVal+val)%26
		index+= 1
		index = 0 if index == len(key) else index
		result+= chr(temp+97)

	print(result)
	file = open("outputMessage.txt","w")
	file.write(result)
	file.close()
	print("Message outputted to file 'outputMessage.txt'")
	return result


def decryptPolyalphabetic(msg):
	msg = msg.lower().replace(" ", "")
	key = str(input("Enter alphabetic key: "))
	if not key.isalpha():
		print("Error: must be alphabetic")
		sys.exit(1)
	result = ""
	index = 0
	val = 0 
	msgVal = 0
	temp = 0
	for i in msg:
		msgVal = ord(i)-97
		val = ord(key[index])-97
		temp = (msgVal-val)%26
		index+= 1
		index = 0 if index == len(key) else index
		result+= chr(temp+97)

	print(result)
	file = open("outputMessage.txt","w")
	file.write(result)
	file.close()
	print("Message outputted to file 'outputMessage.txt'")
	return result

'''
"The Atbash cipher is a substitution cipher with a specific key where the 
letters of the alphabet are reversed. 
I.e. all 'A's are replaced with 'Z's, all 'B's are replaced with 'Y's, and so on. 
It was originally used for the Hebrew alphabet, but can be used for any alphabet."
The Atbash cipher is essentially a substitution cipher with a fixed key, if you know the cipher is Atbash, 
then no additional information is needed to decrypt the message.

References:
https://github.com/CryptoUSF/Course-Material/blob/master/references/books/1911%20-%20Manual%20of%20Cryptography.pdf
http://practicalcryptography.com/ciphers/classical-era/atbash-cipher/

The following functions take in a message to perform encryption/decryption.

Usage: 
[python3] [ciphers.py] [-f doc.txt] [-c5 -e]
[python3] [ciphers.py -f] [outputMessage.txt] [-c5 -d]
'''
def encryptAtbash(msg):
	result = ""
	msg = msg.lower()
	result = ""
	for char in msg:
		temp = char
		if not (char.isspace()):
			if char in letters:
				temp = letters[25-letters.index(char)]
				result += temp
			else:
				result += char
	file = open("outputMessage.txt","w")
	file.write(result)
	file.close()
	print("Message outputted to file 'outputMessage.txt'")
	return result

	return result

def decryptAtbash(msg):
	result = ""
	msg = msg.lower()
	result = ""
	for char in msg:
		temp = char
		if not (char.isspace()):
			if char in letters:
				temp = letters[25-letters.index(char)]
				result += temp
			else:
				result += char
	file = open("outputMessage.txt","w")
	file.write(result)
	file.close()
	print("Message outputted to file 'outputMessage.txt'")
	return result


#Uses argparse to run the program.
def run(arg):
	encrypt = True
	text = ""
	key = 4
	if arg.encrypt and arg.decrypt:
		print("Please select one encrypt/decrypt flag option")
		sys.exit(0)
	if not arg.encrypt and not arg.decrypt:
		print("Please select one encrypt/decrypt flag option")
		sys.exit(0)

	if arg.decrypt:
		encrypt = False

	if(arg.key):
		print(arg.key)
		try:
			if int(arg.key) > 25:
				print("Invalid key")
				return

			else:
				key = int(arg.key)

		except ValueError:
			print("Input not a valid int.")
			return

	if(arg.file):
		try:
			file = open(arg.file, 'r+')
			for lines in file:
				text+=lines
			print("Original message: " +text)

		except IOError:
			print("Cannot read file")
			return

	if encrypt == True:
		if(arg.c1):
			print("New encrypted message: " + encryptCaesar(text, key))
		elif(arg.c2):
			print("New encrypted message: " + encryptSimpleSubstitution(text))
		elif (arg.c3):
			print("New encrypted message: " + encryptPolyalphabetic(text))
		elif(arg.c4):
			print("New encrypted message: " + transpositionEncrypt(text, key))
		elif(arg.c5):
			print("New encrypted message: " + encryptAtbash(text))
	else:
		if(arg.c1):
			print("New decrypted message: " + decryptCaesar(text, key))
		elif(arg.c2):
			print("New decrypted message: " + decryptSimpleSubstitution(text))
		elif (arg.c3):
			print("New decrypted message: " + decryptPolyalphabetic(text))
		elif(arg.c4):
			print("New decrypted message: " + transpositionDecrypt(text, key))
		elif(arg.c5):
			print("New decrypted message: " + decryptAtbash(text))

if __name__ == '__main__':
	arg = func()
	run(arg)
