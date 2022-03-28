import os
import io
from aleatorio import aleatorio

def main():
    alphabet = {
        0: 'a', 1: 'b', 2: 'c', 3:'d', 4:'e', 5:'f', 6:'g',
        7: 'h', 8: 'i', 9: 'j', 10:'k', 11:'l', 12:'m', 13:'n',
        14: 'o', 15: 'p', 16: 'q', 17:'r', 18:'s', 19:'t', 20:'u',
        21: 'v', 22: 'w', 23: 'x', 24:'y', 25:'z',
    }
    f = io.open(os.path.join("./data/cryptography", "cifra_xor_a.txt"), 'r', encoding='windows-1252')
    # f = io.open(os.path.join("./reports", "cifra_xor_a_dec.txt"), 'r', encoding='windows-1252')
    
    content = f.read()
    f.close()
    desc_content = ''

    for i, c in enumerate(content):
        if (c == ' '): desc_content += c
        elif (c == '\n'): desc_content += c
        else:
            
            desc_c = chr(ord(c) ^ (aleatorio()%26))
            desc_content += desc_c

    print(desc_content)

    f = open(os.path.join("./reports", "cifra_xor_a_dec.txt"), 'w')
    # f = open(os.path.join("./reports", "cifra_xor_a_enc.txt"), 'w')
    f.write(desc_content)
    f.close()


if __name__ == '__main__':
    main()