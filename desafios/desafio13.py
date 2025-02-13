def pegaHora(n: str):
    h = [n[0], n[1]]
    m = [n[3], n[4]]
    s = [n[6], n[7]]
    
    hora = h[0] + h[1]
    hora = int(hora)
    minuto = m[0] + m[1]
    minuto = int(minuto)
    segundo = s[0] + s[1]
    segundo = int(segundo)
    
    horaEmMin = hora * 60
    minuto += horaEmMin
    minEmSegundo = minuto * 60
    segundo += minEmSegundo

    return segundo

print(pegaHora("10:00:00"))
