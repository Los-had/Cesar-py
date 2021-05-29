from time import sleep 

modo = ''
resultado = ''
aviso = 'AVISO: este programa so faz a descriptografia em 3 camadas então aqui vai um exemplo: "a" = "d"'
aviso2 = 'AVISO: este programa não suporta caracteres especiais e acentos'

print(aviso)
print(aviso2)

modo = input("1 - Descriptografar\n >  ")

if(modo == '1' or 'd' or 'D' or 'Decrypt' or 'decrypt' or 'Descriptografar' or 'descriptografar'):
    texto = input("Insira o texto para descriptografar \n >  ")
    for i in range (0, len(texto)):
        resultado = resultado + chr(ord(texto[i]) - 3)
print('')
print(resultado)

sleep(20.5)