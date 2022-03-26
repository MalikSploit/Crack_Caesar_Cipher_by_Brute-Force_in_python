'''
We need the alphabet because we convert letter into numerical values to
be able to use mathematical operations (note we encrypt the spaces as well).
'''
ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ' #27 Chacarters because we added the space

def crack_caesar(cipher_text):
    #We make the algorithm case insensitive
    cipher_text = cipher_text.upper()
    #We try all the possible values so the size of the ALPHABET 
    for key in range(len(ALPHABET)):
        #Reinitialize this to be an empty string
        plain_text = ''
        #We just have to make a simple caesar decryption
        for c in cipher_text:
            index= ALPHABET.find(c)
            index = (index - key) % len(ALPHABET)
            plain_text = plain_text + ALPHABET[index]

        #Print the actual ecrypted string with the given key
        print("With key %s, the result is : %s" % (key, plain_text))

if __name__ == '__main__':
    encrypted = 'PdolnCpdnnhv' #Which is Malik Makkes
    crack_caesar(encrypted)
