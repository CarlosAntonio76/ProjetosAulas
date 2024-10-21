"""
Você deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classes:

1) = Motor
2) = Direcao
O Motor terá a responsabilidade de contrloar a velocidade.
Ele oferece os seguintes atributos:
1) = Atributo de dado velocidade
2) = Metodo acelerar, que deverá incrementar a velocidade de uma unidade
3) = Metodo frear que deverá decrementar a velocidade em duas unidades

A Direção terá a responsabilidade de controlar a direcão. Ela oferece os sguintes atributos:
1) = Valor de direção com valores possíveis: Note, Sul, Leste, Oeste.
2) = Metodo girar_a_direita
3) = Metodo girar_a_esquerda

  N
O   l
  s
Exemplo:
# Testando motor
>>> motor = Motor()
>>> motor.velocidade
0
>>> motor.acelerar()
>>> motor.velocidade
1
>>> motor.acelerar()
>>> motor.velocidade
2
>>> motor.acelerar()
>>> motor.velocidade
3
>>> motor.frear()
>>> motor.velocidade
1
>>> motor.frear()
>>> motor.velocidade
0
>>> # Testando Direção
>>> direcao = Direcao()
>>> direcao.valor
'Norte'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Leste'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Sul'
>>> direcao_girar_a_direita()
>>> direcao.valor
'Oeste'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Norte'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Oeste'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Sul'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Leste'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Norte'
>>> carro = Carro(direcao, motor)
>>> carro.calcular_velocidade()
0
>>> carro.acelerar()
>>> carro.calcular_velocidade()
1
>>> carro.acelerar()
>>> carro.calcular_velocidade()
2
>>> carro.frear()
>>> carro.calcular_velocidade()
0
>>> carro.calcular_direcao()
>>> 'Norte'

>>> carro.calcular_direita()
>>> carro.calcular_direcao()
>>> 'Leste'

>>> carro.calcular_esquerda()
>>> carro.calcular_direcao()
>>> 'Norte'

>>> carro.calcular_esquerda()
>>> carro.calcular_direcao()
>>> 'Oeste'
"""

class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)
