import os
from time import sleep
from date import *
from dominio import *

key('esc')
box = find('movimentos', 0.8)
click(box)
click(box)
click(box)
sleep(0.5)
key('esc')
sleep(0.5)
letras = ['r', 'n', 'f', 'e']
for letra in letras:
    write(letra)
    sleep(0.5)
y, m = mes_anterior()
# write(f'{m}/{y}')
first, lasted = first_lasted_day(y, m)
sleep(0.5)

# key('home')
sleep(0.5)
write(f'01/{m}/{y}')
sleep(0.5)
#
write(f'{lasted}/{m}/{y}')

for _ in range(11):
    key('tab')
    sleep(0.1)
write(2)
key('tab')
#

caminho_string = r'Client C (M:\)'
# C:\DOMINIO\1 - SPED ICMS SEM MOV
caminho_valido = os.path.normpath(caminho_string)
caminho_valido = os.path.join(os.path.normpath(caminho_string), 'DOMINIO\1 - SPED ICMS SEM MOV')
# write(caminho_valido)
# sleep(0.5)

key('tab')
# key('enter')

# write(caminho_valido)
# apagar(50)
#   key('enter')
# 01/09/2023
write('e')
sleep(1)

selecao = find('selecao', 0.7)
click(selecao)
sleep(1)
selecao = find('sped', 0.7)
click(selecao)
sleep(0.5)
key('tab')
sleep(0.5)
write('o')
sleep(0.5)
write('o')

selecao = find('export', 0.7)
key()


print('Terminou a execução')


