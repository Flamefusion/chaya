#!/usr/bin/python3
"""
LSB Steganography program in Python 3
Requirements: OpenCV, NumPy, Crypography
"""
from cv2 import imread,imwrite
import numpy as np
from base64 import urlsafe_b64encode
from hashlib import md5
from cryptography.fernet import Fernet

#Returns text representation of a binary string
def bin2str(string):
    return ''.join(chr(int(string[i:i+7],2)) for i in range(len(string))[::7])

#Returns binary representation of a string
def str2bin(string):
    return ''.join((bin(ord(i))[2:]).zfill(7) for i in string)

#Returns the encrypted/decrypted form of string depending upon mode input
def encrypt_decrypt(string,password,mode='enc'):
    _hash = md5(password.encode()).hexdigest()
    cipher_key = urlsafe_b64encode(_hash.encode())
    cipher = Fernet(cipher_key)
    if mode == 'enc':
        return cipher.encrypt(string.encode()).decode()
    else:
        return cipher.decrypt(string.encode()).decode()