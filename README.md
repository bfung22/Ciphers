## Crypto Ciphers
#### Author: Benny Fung

### Python program that utilises five different cipher algorithms to encrypt/decrypt a given file.
### The following ciphers include:

- Caesar cipher
- Simple substitution cipher
- Poly-alphabetic cipher
- Transposition cipher
- Atbash cipher

When encrypted/decrypted, the message gets outputted to a new text file.

### This program utilises argument parser, and the flags are as follow:
> - '-e' or "--encrypt" flag to encrypt a file
>- '-d' or "--decrypt" flag to decrypt a file
>- '-k' or '--key' flag to input key for certain cipher functions
>- '-c1' or '--c1' flag to run the Caesar cipher
>- '-c2' or '--c2' flag to run the Simple substitution cipher
>- '-c3' or '--c3' flag to run the Poly-alphabetic cipher
>- '-c4' or '--c4' flag to run the Transposition cipher
>- '-c5' or '--c5'
>- '-f' or '--file' to input text file
>- 'h' for usage help

### Example usage:
- [python3] [ciphers.py] [-e] [-f file.txt] [c1] [-k 5]
- [python3] [ciphers.py] [-d] [-f file.txt] [c1] [-k 5]


### Main references used (more listed in file):

https://github.com/CryptoUSF/Course-Material/blob/master/references/books/1911%20-%20Manual%20of%20Cryptography.pdf

https://www.tutorialspoint.com/cryptography/traditional_ciphers.htm
