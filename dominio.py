import pyautogui
from time import sleep
from date import *
# from start import start

# start()


def find(img, confidence=0.9):
    while 1:
        box = (0, 0, 0, 0)
        try:
            box = pyautogui.locateOnScreen(f'imgs/{img}.png', confidence=confidence)
            # print(box)
            if box[0]:
                return box
        except:
            continue  # não achou imagem


def apagar(numero=30):
    for _ in range(numero):
        pyautogui.press('delete')
        sleep(0.1)


def write(text):
    text = str(text)
    pyautogui.typewrite(text)


def click(box, point="centro"):
    x, y = 0, 0

    if point == "centro":
        x = box.left + box.width / 2
        y = box.top + box.height / 2
    elif point == "topo":
        x = box.left + box.width / 2
        y = box.top
    elif point == "esquerda":
        x = box.left
        y = box.top + box.height / 2
    elif point == "direita":
        x = box.left + box.width
        y = box.top + box.height / 2
    elif point == "inferior":
        x = box.left + box.width / 2
        y = box.top + box.height

    pyautogui.click(x, y)


def key(key='enter'):
    pyautogui.press(key)


def login(user='gerente', senha='123'):
    box = find('login', 0.7)
    click(box, 'topo')
    # print('click no login')
    apagar(10)
    write(user)
    key('tab')
    write(senha)
    key('enter')


def click_custom(box, x_percent, y_percent):
    x = box.left + box.width * x_percent/10
    y = box.top + box.height * y_percent/10
    pyautogui.click(x, y)

if __name__ == '__main__':
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
        write('g')
        # se chegou aqui é porque achou a imagem
        fim = find('fim')
        write('n')

        print('Terminou a execução')
