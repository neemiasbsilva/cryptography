import os


def mapping_content(content):
    frequency_mapping = {
        'e': .1463, 'b': .0104, 'c': .0388, 'u': .0499, 'a': .1257, 'f': .0102,
        'g': .0130, 'h': .0128, 'i': .0618, 'j': .0040, 'k': .0002, 'p': .0278,
        'm': .0474, 't': .0505, 'o': .1073, 'l': .0252, 'q': .0120, 'd': .0653,
        's': .0781, 'n': .0434, 'r': .0463, 'v': .0167, 'w': .0001, 'x': .0021, 
        'y': .0001, 'z': .0047
    }
    frequency_mapping = dict(sorted(frequency_mapping.items(), key=lambda item: item[1], reverse=True))
    mapping = list(frequency_mapping.keys())

    content = content.replace('\n', '')
    content = content.replace(',', '')
    content = content.replace('.', '')
    words = content.split(' ')

    frequency_digraph = {}

    for w in words:
        if (len(w) == 2 and not w in frequency_digraph):
            frequency_digraph[w] = 1
        elif (len(w) == 2):
            frequency_digraph[w] += 1
        else:
            sub_words = [w[i:i+2] for i in range(0, len(w), 2)]
            for s_w in sub_words:
                if (s_w.isalnum() and not s_w.isnumeric() and not s_w in frequency_digraph):
                    frequency_digraph[s_w] = 1
                elif (s_w.isalnum()and not s_w.isnumeric()):
                    frequency_digraph[s_w] += 1

    frequency_digraph = dict(sorted(frequency_digraph.items(), key=lambda item: item[1], reverse=True))

    frequency = {}
    for i, key in enumerate(frequency_digraph):
        if (i == len(mapping)): break
        frequency[key] = mapping[i]


    return frequency


def descryptrography(frequency_dict, content):
    content = content.replace('\n', '')
    content = content.replace(',', '')
    content = content.replace('.', '')
    words = content.split(' ')

    for key in frequency_dict:
        content = content.replace(key, frequency_dict[key])
    
    return content


def main():
    f = open(os.path.join("./data/cryptography","carta.txt"), 'r')
    content = f.read()

    frequency_dict = mapping_content(content)
    content_dec = descryptrography(frequency_dict, content)
    
    f = open(os.path.join("./reports", "carta_dec.txt"), 'a')
    f.write(content_dec)
    f.close()

if __name__ == '__main__':
    main()
    