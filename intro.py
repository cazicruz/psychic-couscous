#!/usr/bin/env/python3
""" An encryption program that collects input from a user and a key where the key is used to shift the ascii code by
+ or - the key """


def main():
    """ main body of program"""
    user_input = input("please type in some text")
    user_key = ord(input("please specify a key to encode your message with"))

    ascii_of_usr_input = text_to_ascii(user_input)
    encoded_ascii_str = list_encoder_with_key(ascii_of_usr_input, user_key)
    encoded_text = ascii_to_text(encoded_ascii_str)

    print(encoded_text)

    decoded_text = decoder_with_key(encoded_ascii_str, user_key)

    for ch in decoded_text:
        print(ch, end='')


def text_to_ascii(user_text):
    """ converts text to ascii code"""
    ascii_value_of_input = []
    for ch in user_text:
        ascii_value_of_input.append(ord(ch))
    return ascii_value_of_input


def list_encoder_with_key(ascii_code, key):
    """ checks if the item is within the ascii values for alphabets"""
    ''' Else its a special character so append it unaffected by key'''
    encoded_str = []
    for item in ascii_code:
        item_mod = item - 32
        encoded_str.append(item_mod + key)
    return encoded_str


def ascii_to_text(text_input):
    """converts ascii codes to texts"""
    ascii_text = []
    for item in text_input:
        ascii_text.append(chr(item))
    return ascii_text


def decoder_with_key(encoded_str, key):
    """ use key to decode message """
    decoded_str = []
    for ch in encoded_str:
        ch_mod = ch + 32
        decoded_str.append(chr(ch_mod - key))
    return decoded_str