# uma funcao que receba um numero de 1 a 26 e retorne uma array com as letras do alfabeto
def alfa(num):
    letras = "ABCDEFGIJKLMNOPQRSTUVWXYZ"
    if 1 <= num <=len(letras):
        return " ".join(letras[:num])
    else:
        return "pode nao"
print(alfa(26))