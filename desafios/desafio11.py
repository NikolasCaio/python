def inverte_string(texto):
    invertida = ""
    for letra in texto:
        invertida = letra + invertida
    return invertida

print(inverte_string('xesquedele'))