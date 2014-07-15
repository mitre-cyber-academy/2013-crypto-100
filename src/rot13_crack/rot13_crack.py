#!/usr/bin/env python

import sys
import frequency_analysis

def main():
    dictionary = open('./dictionary.txt', 'r').read().split()
    ciphertext = open('./rot13_ciphertext.txt', 'r').read()
    cipherlist = list(ciphertext)
    analyser   = frequency_analysis.Frequency('./rot13_ciphertext.txt')
    length, alpha_dict, freq_dict = analyser.analyze()
    frequencies = [(item, freq_dict[item]) for item in freq_dict]
    frequencies.sort(key=lambda tup: tup[1])
    frequencies.reverse()
    r_dict    = set_up_replace_dict(cipherlist, frequencies)
    while True:
        plaintext = ''
        for byte in cipherlist:
            try:
                plaintext += r_dict[byte]
            except KeyError:
                plaintext += byte
        print plaintext
        for item in r_dict:
            print('%s  ->  %s' %(item, r_dict[item]))
        user_input = raw_input('Correct a letter? ')
        if user_input == '':
            break
        else:
            first         = user_input.split()[0]
            second        = user_input.split()[1]
            for item in r_dict:
                if r_dict[item] == first:
                    r_dict[item] = second
                    r_dict[first] = item
                    break
    open('out.txt', 'w').write(plaintext)

def set_up_replace_dict(cipherlist, frequencies):
    r_dict = {'a':'', 'b':'', 'c':'',
              'd':'', 'e':'', 'f':'',
              'g':'', 'h':'', 'i':'',
              'j':'', 'k':'', 'l':'',
              'm':'', 'n':'', 'o':'',
              'p':'', 'q':'', 'r':'',
              's':'', 't':'', 'u':'',
              'v':'', 'w':'', 'x':'',
              'y':'', 'z':''}
    sorted_alphabet = ['e', 't', 'a', 'o', 'i', 'n',
                       's', 'h', 'r', 'd', 'l', 'c',
                       'u', 'm', 'w', 'f', 'g', 'y',
                       'p', 'b', 'v', 'k', 'j', 'x',
                       'q', 'z']
    for number in range(len(frequencies)):
        r_dict[frequencies[number][0]] = sorted_alphabet[number]
    return r_dict

def shift_byte(byte, shift):
    nRangeByte = (ord(byte) + 7) % 26
    encoded_byte = chr(((nRangeByte - shift) % 26) + 97)
    return encoded_byte

if __name__ == "__main__":
    sys.exit(main())
