from time import sleep
from date import *
from dominio import *


#start_dominio()
# box = find('fiscal')
sleep(1)
# click(box)
# sleep(1)
# key()
# sleep(5)
# login()
box = find('escrita', 0.7)
click(box)
# box = find('escrita')
#click_custom(box, 0.5, 0.5)
box = find('movimentos', 0.8)
click(box)
write('r')
sleep(1)

y, m  = mes_anterior()
write(f'{m}/{y}')
key('tab')
write(f'{m}/{y}')
sleep(1)
key('tab')
sleep(1)
write('g')
# se chegou aqui é porque achou a imagem

fim = find('aviso')
key('esc')
fim = find('fim')
write('n')
key('esc')
print('Terminou a execução')    