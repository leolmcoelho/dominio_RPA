from datetime import datetime, timedelta
import calendar

def day_now():
    data_atual = datetime.now()
    dia = data_atual.strftime('%d')
    mes = data_atual.strftime('%m')
    ano = data_atual.strftime('%Y')
    return ano, mes, dia


def mes_anterior():
    data_atual = datetime.now()
    data_anterior = data_atual - timedelta(weeks=4)  # Subtrai 1 dia
    ano_anterior = data_anterior.strftime('%Y')
    mes_anterior = data_anterior.strftime('%m')
    return ano_anterior, mes_anterior


def first_lasted_day(ano, mes):
    # Use o módulo calendar para obter o primeiro e o último dia do mês
    ano_i = int(ano)
    mes_i = int(mes)
    primeiro_dia = f'01/{mes}/{ano}'
    ultimo_dia = f'{calendar.monthrange(ano_i, mes_i)[1]}'  # Último dia do mês

    return primeiro_dia, ultimo_dia


if __name__ == '__main__':
    a = mes_anterior()
    print(a)
    y, m = mes_anterior()

    first, lasted = first_lasted_day(y, m)
    print(f'{lasted}/{m}/{y}')