import math

# Atividade - 🧠 Lógica - Exercitando Funções e Builtins
# Você deverá criar duas funções, delta e bhaskara, seguindo as orientações:

# bhaskara
# delta


def bhaskara(a, b, c):
    elevado = b**2
    multiplicador = 4 * a * c
    delta = elevado - multiplicador
    if delta < 0:
        return print("Delta Negativo")
    else:
        print(f"x1= {bhaskara_x1(a, b, delta)}")
        print(f"x2= {bhaskara_x2(a, b, delta)}")


def bhaskara_x1(a, b, delta):
    raiz_de_delta = math.sqrt(delta)
    subtracao_de_b = -b + raiz_de_delta
    mutiplicacao_de_a = 2 * a
    x1 = round(subtracao_de_b / mutiplicacao_de_a, 2)
    return x1


def bhaskara_x2(a, b, delta):
    raiz_de_delta = math.sqrt(delta)
    subtracao_de_b = -b - raiz_de_delta
    mutiplicacao_de_a = 2 * a
    x2 = round(subtracao_de_b / mutiplicacao_de_a, 2)
    return x2


bhaskara(3, 10, 2)
