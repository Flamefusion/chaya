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

def encode(input_filepath,text,output_filepath,password=None):
    if password != None:
        data = encrypt_decrypt(text,password,'enc') #If password is provided, encrypt the data with given password
    else:
        data = text #else do not encrypt
    data_length = bin(len(data))[2:].zfill(32) #get length of data to be encoded
    bin_data = iter(data_length + str2bin(data)) #add length of data with actual data and get the binary form of whole thing
    img = imread(input_filepath,1) #read the cover image
    if img is None:
        raise FileError("The image file '{}' is inaccessible".format(input_filepath)) #if image is not accessible, raise an exception
    height,width = img.shape[0],img.shape[1] #get height and width of cover image
    encoding_capacity = height*width*3 #maximum number of bits of data that the cover image can hide
    total_bits = 32+len(data)*8 #total bits in the data that needs to be hidden including 32 bits for specifying length of data
    if total_bits > encoding_capacity:
        raise DataError("The data size is too big to fit in this image!") #if cover image can't hide all the data, raise DataError exception
    completed = False
    modified_bits = 0
    
    #Run 2 nested for loops to traverse all the pixels of the whole image in left to right, top to bottom fashion
    for i in range(height):
        for j in range(width):
            pixel = img[i,j] #get the current pixel that is being traversed
            for k in range(3): #get next 3 bits from the binary data that is to be encoded in image
                try:
                    x = next(bin_data)
                except StopIteration: #if there is no data to encode, mark the encoding process as completed
                    completed = True
                    break
                if x == '0' and pixel[k]%2==1: #if the bit to be encoded is '0' and the current LSB is '1'
                    pixel[k] -= 1 #change LSB from 1 to 0
                    modified_bits += 1 #increment the modified bits count
                elif x=='1' and pixel[k]%2==0: #if the bit to be encoded is '1' and the current LSB is '0'
                    pixel[k] += 1 #change LSB from 0 to 1
                    modified_bits += 1 #increment the modified bits count
            if completed:
                break
        if completed:
            break

    written = imwrite(output_filepath,img) #create a new image with the modified pixels
    if not written:
        raise FileError("Failed to write image '{}'".format(output_filepath))
    loss_percentage = (modified_bits/encoding_capacity)*100 #calculate how many bits of the original image are changed in order to encode the secret message and calculate the percentage of data loss from it
    return loss_percentage