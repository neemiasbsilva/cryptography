import numpy as np

def load_file(path: str):
    file = open(path, 'r')
    content = file.read()
    file.close()
    return content


def generate_viginere_squared():
    viginere_squared = np.zeros(shape=(26, 26), dtype=np.int32)

    for i in range(26):
        for j in range(26):
            if (i == 0):
                viginere_squared[i, j] = j
            else:
                if (j < 25):
                    viginere_squared[i, j] = viginere_squared[i-1, j+1]
                else:
                    viginere_squared[i, j] = viginere_squared[i-1, 0]

    return viginere_squared


def decryptography(content, viginere_squared, symbols, key="emily"):
    val_list = list(symbols.values())
    key_index = [val_list.index(w) for w in key]
    i = 0
    dec_content = ''
    for e in content:
        if (e == '\n' or e.isspace()):
            dec_content += e
        else:
            if (i < len(key_index)):
                value = val_list.index(e)
                j = list(viginere_squared[key_index[i]]).index(value)
                dec_content += symbols[j]
            else:
                i = 0
                value = val_list.index(e)
                j = list(viginere_squared[key_index[i]]).index(value)
                dec_content += symbols[j]

            i += 1

    return dec_content


def save_file(path, content):
    f = open(path, 'w')
    f.write(content)
    f.close()


def main():
    symbols = {
        0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g',
        7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n',
        14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u',
        21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z',
    }
    content = load_file("data/cryptography/poema_cifrado.txt")
    # content = content.replace('\n', '')
    # content_list = content.split(' ')
    viginere_squared = generate_viginere_squared()
    dec_content = decryptography(content, viginere_squared, symbols)
    save_file("reports/poema.txt", dec_content)


if __name__ == '__main__':
    main()
    