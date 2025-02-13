'''def removerSubstring(texto: str, subtexto: str):
    posicao_do_subtexto = texto.find(subtexto) 
    resultado = ""

    for i in range(len(texto)):
        if posicao_do_subtexto != -1 and posicao_do_subtexto <= i < posicao_do_subtexto + len(subtexto):
            continue
        resultado += texto[i]

    return resultado

print(removerSubstring('O CriaScript eh um mamaco, CriaScript'))   
'''
def remover_substring(texto: str, subtexto: str) -> str:
    return texto.replace(subtexto, "")

print(remover_substring("O CriaScript eh um manaco", "CriaScript"))
