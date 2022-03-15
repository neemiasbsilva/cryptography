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


def encryptography(content, viginere_squared, symbols, key="emily"):
    val_list = list(symbols.values())
    key_index = [val_list.index(w) for w in key]
    i = 0
    enc_content = ''
    for e in content:
        if (e == '\n' or e.isspace()):
            enc_content += e
        else:
            if (i < len(key_index)):
                j = val_list.index(e)
                enc_content += symbols[viginere_squared[key_index[i], j]]
            else:
                i = 0
                j = val_list.index(e)
                enc_content += symbols[viginere_squared[key_index[i], j]]

            i += 1

    return enc_content


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
    content = load_file("data/cryptography/poema.txt")
    # content = content.replace('\n', '')
    # content_list = content.split(' ')
    viginere_squared = generate_viginere_squared()
    enc_content = encryptography(content, viginere_squared, symbols)
    save_file("reports/poema_encriptado.txt", enc_content)


if __name__ == '__main__':
    main()
    