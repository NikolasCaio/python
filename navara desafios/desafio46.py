from time import sleep

print('Contagem regressiva dos fogos de artificio em')
for c in range(10, -1, -1):
    print(c)
    sleep(0.5)
print('BUMM!!')