import os

def main():
    f = open(os.path.join("./data/cryptography", "misterio.txt"), 'r')
    shift = 3
    content = f.read()
    f.close()
    desc_content = ''
    for c in content:
        if (c == ' '): desc_content += c
        elif (c == '\n'): desc_content += c
        elif (ord(c) < 100): 
            flag_1 = abs(ord(c)- ord('a'))
            flag_2 = abs(flag_1-shift)
            temp = chr(ord('z')-flag_2)
            if (temp == 'w'): desc_content += 'x'
            elif (temp == 'y'): desc_content += 'z'
            else: desc_content += temp
        else:
            desc_content += chr(ord(c)-shift)
    
    f = open(os.path.join("./reports", "misterio_dec.txt"), 'w')
    f.write(desc_content)
    f.close()

if __name__ == '__main__':
    main()
    