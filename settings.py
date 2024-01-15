# gravar information basicas  para uso do sistema
##################################################
import pcc

# CAMINHO_ARQUIVO = 'c:/Users/sandr/Sandro_py/venv/PCC/settings.json'
CAMINHO_ARQUIVO = pcc.CAMINHO_ARQUIVO_SETTINGS
print(CAMINHO_ARQUIVO)


lista = pcc.carregar_dados_arquivo([], CAMINHO_ARQUIVO)

print(f' Valor atual da hora : {lista[0]}')
print(f' Periodo atual de {lista[1]} dais')

sn = input('Deseja realmente alterar ? s/n ') or 's'
if sn == 's':

    while True:
        salario = input('Informe seu salario por hora: ')
        try:
            salario = float(salario)
            break
        except:
            print('Valor invlido...')

    while True:
        intervalo = input('Informe de quantos dias e o periodo: ')
        try:
            intervalo = int(intervalo)
            break
        except:
            print('intervalo invlido...')

        break
    pcc.salvar_dados([salario, intervalo], CAMINHO_ARQUIVO)

    lista = pcc.carregar_dados_arquivo([], CAMINHO_ARQUIVO)
else:
    print('Saindo...')
