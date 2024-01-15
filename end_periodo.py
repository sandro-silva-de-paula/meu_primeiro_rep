# encerrar periodo, renomear aquivo para envio
##############################################
import os
import pcc
import json
from datetime import date, time, datetime, timedelta


settings = pcc.carregar_dados_arquivo([], pcc.CAMINHO_ARQUIVO_SETTINGS)
periodo = pcc.carregar_dados_arquivo([], pcc.CAMINHO_ARQUIVO)
horas = timedelta(minutes=0)

print(pcc.CAMINHO_ARQUIVO.parent)

sn = input('Confirma finalizacao do periodo? s/n  ') or 'n'

if sn.upper() == 'S':

    if len(periodo) > 0:

        ini_cio = periodo[0]
        ini_cio = str(ini_cio[0])
        ini_cio = ini_cio.split('/')
        ini_cio = ini_cio[0]+ini_cio[1]+ini_cio[2]

        fi_nal = periodo.pop()
        fi_nal = str(fi_nal[0])
        fi_nal = fi_nal.split('/')
        fi_nal = fi_nal[0]+fi_nal[1]+fi_nal[2]

        new_name = os.path.join(pcc.CAMINHO_ARQUIVO.parent,
                                ini_cio+'_'+fi_nal+'.json')

        print('Encerrando periodo atual.')
        print('Criando arquivo para remessa...')
        try:
            os.rename(pcc.CAMINHO_ARQUIVO, new_name)
            print(f'Arquivo gerado: {new_name} ')
        except:
            print(f'Algum erro ocorreu ao tentar criar arquivo {new_name}')

        # buscar inf do
        periodo = pcc.carregar_dados_arquivo([], new_name)
        for i in periodo:
            horas += datetime.strptime(i[2], '%H:%M') - \
                datetime.strptime(i[1], '%H:%M')

        minutos = (horas.total_seconds()/60)
        valor_minuto = settings[0]/60

        lista_resumo = [minutos, round(minutos*valor_minuto, 2)]
        periodo.append(lista_resumo)

        with open(new_name, 'w', encoding='utf8') as arquivo:
            json.dump(periodo, arquivo, indent=2, ensure_ascii=False)
    else:
        print('Periodo nao iniciado')
else:
    print('Saindo...')
