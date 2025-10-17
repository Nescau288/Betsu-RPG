print('Olá, vamos fazer o calculo desse bagulho kkkk')
I = int(input('Me diga a sua INTELIGÊNCIA?\nDigite aqui: '))
# print('Burro pra krai kkkkk')

Ca = int(input('Agora o CARISMA?\nDigite aqui: '))
# print('O cara não sabe socializar kkkkk')

F = int(input('Sobre a FORÇA?\nDigite aqui: '))
# print('Não consegue levantar um galão de água kkkkkkk')

A = int(input('Me diga agora a sua AGILIDADE?\nDigite aqui: '))
# print('Não consegue fugir de uma lesma kkkkkk')

Co = int(input('Por último, sobre sua CONSTITUIÇÃO?\nDigite aqui: '))
#print('Vou nem comentar...')

nivel = int(input('Agora, me diga o seu nível (começando do nível 1): '))

N = nivel - 1

print('Vamos calcular os seus status agora: ')
mana = 20 + (5 * I) + (10 * N)  # +10 de mana por nível
vida = 20 + (5 * Co) + (5 * N)   # +5 de vida por nível
stamina = 20 + 5 * (A + F) + (10 * N)  # +10 de stamina por nível
Fr = ((I*Ca)*nivel)

print('='*20)
print('Sua MANA inicial é: \033[32m{}\033[0m'.format(mana))
print('Sua VIDA inicial: \033[32m{}\033[0m'.format(vida))
print('Sua STAMINA é: \033[32m{}\033[0m'.format(stamina))
print('Seu FIO DE RAZÃO é \033[32m{}\033[0m'.format(Fr))
print('='*20)

print('Agora sobre suas resistência...')
rf = Co + F * 2
rm = Co + I

print('='*20)
print('Sua RESISTÊNCIA FÍSICA é: \033[32m{}\033[0m'.format(rf))
print('Sua RESISTÊNCIA MÁGICA é: \033[32m{}\033[0m'.format(rm))
print('='*20)

print('Agora sobre sobre os alcances...')
m = 3 + A
am = 4 + I
af = 1

print('='*20)
print('Sua MOVIMENTAÇÃO é: \033[32m{}\033[0m'.format(m))
print('Seu ALCANCE MÁGICO é: \033[32m{}\033[0m'. format(am))
print('Seu ALCANCE FÍSICO é: \033[32m{}\033[0m'.format(af))