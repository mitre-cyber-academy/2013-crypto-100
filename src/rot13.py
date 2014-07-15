#!/usr/bin/env python

import sys
import argparse

def main():
    args         = get_args()
    encoded_text = encode(args)
    print encoded_text

def encode(args):
    '''
    Create a (ciphertext|plaintext) from given args
    :param dictionary: args
    '''
    text       = clean(args.message)
    ciphertext = ''
    for byte in text:
        ciphertext += shift_byte(byte, args.shift, args.decrypt)
    return ciphertext

def shift_byte(byte, shift, decrypt):
    '''
    Shift given byte the given amount in the given direction.
    :param string: byte
    :param int: shift
    :param bool: decrypt
    '''
    # Convert the letter range from [97,122] to [0,26]
    nRangeByte = (ord(byte) + 7) % 26
    # Shift and convert back to [97,122]
    if decrypt:
        encoded_byte = chr(((nRangeByte - shift) % 26) + 97)
    else:
        encoded_byte = chr(((nRangeByte + shift) % 26) + 97)
    return encoded_byte

def clean(message):
    '''
    Clean message so that it's restricted to lowercase alphabetic characters
    :param dictionary: args
    '''
    dirty_text = list(message)  # Convert to list
    def num_det(letter):  # Small helper function to prune
        # If the letter is in the correct range, return it
        if ord(letter.lower()) >= 97 and ord(letter.lower()) <= 122:
            return letter.lower()
        else:
            return ''
    # Clean text is the joined list resulting from our helper function
    clean_text = ''.join([num_det(char) for char in dirty_text])
    return clean_text

def get_args():
    default = '''the quick BROWN fox lept OVER\
    the lazy DOG_1234568790=_=-=_+_+\][|}{~`!@#$%^&*():/.,?><'''
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--message', type=str,
                        default=default, help='Input Message')
    parser.add_argument('-d', '--decrypt', action='store_true',
                        help='Decrypt?')
    parser.add_argument('-e', '--encrypt', action='store_true',
                        help='Encrypt?')
    parser.add_argument('-f', '--fileinput', type=str,
                        default=None, help='Input File')
    parser.add_argument('-s', '--shift', type=int,
                        default=13, help='How far to shift')
    args = parser.parse_args()
    if args.decrypt and args.message == default:
        args.message = 'gurdhvpxoebjasbkyrcgbiregurynmlqbt'
    if args.fileinput:
        args.message = open(args.fileinput, 'r').read()
    return args


if __name__=="__main__":
    sys.exit(main())
