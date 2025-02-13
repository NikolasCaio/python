def equacao_de_segundo_grau(a, b, c):
    if a == 0:
        return "Pode nao"

    equacao = f'{a}x²'

    if b > 0:
        equacao += f" + {b}x"
    elif b < 0:
        equacao += f" -  {-b}x"

    if c > 0:
        equacao += f" + {c}"
    elif c < 0:
        equacao += f" - {-c}"
    equacao += " = 0"

    return equacao

print(equacao_de_segundo_grau(1, -3, 2))