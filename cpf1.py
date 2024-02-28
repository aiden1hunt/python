cpf_usuario = '74682489070'
nove_digitos = cpf_usuario[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito)* contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1*10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0 

dez_digitos = nove_digitos + str(digito)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 0
digito_2 = (resultado_digito_2*10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

novo_cpf_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_usuario == novo_cpf_calculo:
    print(f'{cpf_usuario} é válido')
else:
    print('cpf inválido')