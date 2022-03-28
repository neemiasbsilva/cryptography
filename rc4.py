import io
import numpy as np
import os

i = 0
j = 0

#-------------------------------------------------------------------
# Funcao para transformar {a, b, c, ... z} para {0, 1, 2, ..., 25}:
def map_num (char):
   return ord(char)

#-------------------------------------------------------------------
# Funcao para transformar {0, 1, 2, ..., 25} para {a, b, c, ... z}:
def map_char (num):
   return chr(num)

def KSA (chave, S, N):
   j=0
   for i in range(0, N):
      S[i] = i
   for i in range(0, N):
      j = ((j+S[i]+ord(chave[i % len(chave)]))% N)
      # Update S[i] and S[j]
      S[i], S[j] = S[j], S[i]
   return S
   

def PRGA (S, N):
   global i, j
   i = (i + 1) % N
   j = (j + S[i]) % N
      
   # Update S[i] and S[j]
   S[i], S[j] = S[j], S[i]
   t = (S[i]+S[j]) % N
   return S[t]


#-------------------------------------------------------------------
file = open("./data/cryptography/cifrado.txt", 'r', encoding="utf8")
# file = io.open(os.path.join("./data/cryptography", "cifrado.txt"), 'r', encoding='windows-1252')
# content = file.read()
desc_out = ''
chave = "rodrigo"
N = 256
S = [0] * N
S = KSA(chave, S, N)
with open("./data/cryptography/cifrado.txt", 'r', encoding = 'unicode_escape') as file: 
   for line in file:
      for char in line:
         #Nao modifique o intervalo do caractere em c, nem trate espacos ou nova linha!
         desc_out += chr(ord(map_char(map_num(char))) ^ PRGA(S, N))
         # print(("%c") % (map_char(map_num(char) ^ PRGA(S, N))))
      desc_out += '\n'
print(desc_out)