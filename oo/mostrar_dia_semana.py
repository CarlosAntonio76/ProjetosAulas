'''
Tente criar uma classe que mostre nome do dia da semana

# Inicio
>>> semana = MostrarDiaSemana()
>>> semana.mostrar_nome_semana()
'''

import locale
import datetime
locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')
dia_semana = datetime.datetime.today().weekday()

SEGUNDA = 'Segunda-Feira'
TERCA = 'Terça-Feira'
QUARTA = 'Quarta-Feira'
QUINTA = 'Quinta-Feira'
SEXTA = 'Sexta-Feira'
SABADO = 'Sábado'
DOMINGO = 'Domingo'


class MostrarDiaSemana:
    nome_dia_semana = {
        0: SEGUNDA, 1: TERCA, 2: QUARTA, 3: QUINTA,
             4: SEXTA, 5: SABADO, 6: DOMINGO
        }

    def __init__(self):
        self.numero_semana = dia_semana

    def mostrar_nome_semana(self):
        self.numero_semana = self.nome_dia_semana[self.numero_semana]


if __name__=='__main__':
    semana = MostrarDiaSemana()
    print(semana.nome_dia_semana)
    print(f'Número dia semana: {semana.numero_semana}')
    print(f'Hoje é: {semana.nome_dia_semana[semana.numero_semana]}')











