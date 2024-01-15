import pcc
#descobrir maneira de pesquisar arquivo
lista = pcc.carregar_dados_arquivo([],'c:/Users/sandr/Sandro_py/venv/PCC/09172023 - (Sun)_09232023 - (Sat).json')

resumo = lista.pop()

print(f'Total de horas: {pcc.montar_hora(resumo[0])} --- Valor a receber :{resumo[1]} ')
for dia in lista:
    print(dia)