# Entrada de medida em metros
medida = float(input('Distância em metros: '))

# Conversões para diferentes unidades
km = medida / 1000  # Quilômetros
hm = medida / 100   # Hectômetros
dam = medida / 10   # Decâmetros
dm = medida * 10    # Decímetros
cm = medida * 100   # Centímetros
mm = medida * 1000  # Milímetros

# Exibe as conversões
print('A medida de {} metros corresponde a:'.format(medida))
print('{} km (quilômetros)'.format(km))
print('{} hm (hectômetros)'.format(hm))
print('{} dam (decâmetros)'.format(dam))
print('{} dm (decímetros)'.format(dm))
print('{} cm (centímetros)'.format(cm))
print('{} mm (milímetros)'.format(mm))
