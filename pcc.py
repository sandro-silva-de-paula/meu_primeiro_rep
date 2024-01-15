
# PCC - Payment Check Control
# contagem da horas
###########################
from os import times
from pathlib import Path
import json
from datetime import date, time, datetime, timedelta
from functools import reduce
import os


CAMINHO_ARQUIVO = Path(__file__).parent / 'periodo.json'
CAMINHO_ARQUIVO_SETTINGS = Path(__file__).parent / 'settings.json'

# teste git


def git():
    return


def teste():

    ...


def carregar_dados_arquivo(lista, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe, criando arquivo...')
        salvar_dados(lista, caminho_arquivo)
    return dados


def salvar_dados(lista, caminho_arquivo):
    dados = lista
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(lista, arquivo, indent=2, ensure_ascii=False)
    return dados


def criar_periodo():
    while True:
        try:
            hoje_str = input('Digite a data inicial do periodo (MM/DD/YY): ')
            hoje_dtt = datetime.strptime(hoje_str, "%m/%d/%y")
            break
        except:
            print("Data invalida...")
            continue

    for i in range(settings[1]):
        dias.append([(hoje_dtt + timedelta(days=i)).strftime('%m/%d/%Y - (%a)'),
                     time(0).strftime('%H:%M'),
                     time(0).strftime('%H:%M'),
                     '', ''])

    salvar_dados(dias, CAMINHO_ARQUIVO)
    mostrar_lista()


def mostrar_lista():
    os.system('cls')
    horas = timedelta(minutes=0)

    # montar cabecalho
    print(
        f'PCC - Payment Check Control (v.Beta)              {datetime.now().date()}')
    print(f'Periodo de {settings[1]} dias ')
    print('-'*75)
    print('              DATA --------   IN  --  OUT -- TIME')
    for i, dia in enumerate(dias):
        print('-'*75)
        print(
            f'Day {i+1} - {dia[0]} - {dia[1]} - {dia[2]} - {dia[3]} {dia[4]} ')
        horas += datetime.strptime(dia[2], '%H:%M') - \
            datetime.strptime(dia[1], '%H:%M')
    print('-'*75)

    if horas.total_seconds() > 0:
        minutos = horas.total_seconds()/60
        hora = montar_hora(minutos)
        valor_minuto = settings[0]/60
        print(f'Horas acumuladas: {hora}')
        print(f'Valor Total: { round(minutos*valor_minuto,2)}')


def montar_hora(minutos):
    # verificar hora e minuto quando menor que 10
    hora = minutos // 60
    if hora >= 10:
        hora = str(hora)
        hora = hora[0:2]
    else:
        hora = str(hora)
        hora = '0' + hora[0]

    minuto = minutos % 60
    if minuto >= 10:
        minuto = str(minuto)
        minuto = minuto[0:2]
    else:
        minuto = str(minuto)
        minuto = '0' + minuto[0]

    hora_str = hora + ':' + minuto
    return hora_str


def incluir_horas():
    while True:

        dia_escolhido = input('Informe o dia desejado:(ou Exit para sair) ')

        if dia_escolhido.upper() == 'EXIT':
            print('Saindo...')
            return 'sair'

        # validar se entrou com um numero
        if not dia_escolhido.isdigit():
            print('Entrada invalida ...')
            continue
        if int(dia_escolhido)-1 > len(dias):
            print('Fora da lista...')
            continue
        else:
            break

    atual = dias[int(dia_escolhido)-1]
    print(
        f'Day - {atual[0]} - Entrada: {atual[1]} - Saida: {atual[2]} - {atual[3]}')

    while True:
        try:
            h_ini, m_ini = input('Entrada: (hh:mm) ').split(':')
            # validar dados hora 0...23 min 0..59
            if not h_ini.isdigit() or not m_ini.isdigit():
                print("Entrada invalida...")
                continue

            if int(h_ini) not in range(24) or int(m_ini) not in range(60):
                print('Entrada invalida...')
                continue
            break
        except:
            print('hora invalida')
            continue

    while True:
        try:
            h_fim, m_fim = input('Saida: (hh:mm) ').split(':')
            # validar dados hora 0...23 min 0..59
            if not h_fim.isdigit() or not m_fim.isdigit():
                print("Saida invalida...")
                continue

            if int(h_fim) not in range(24) or int(m_fim) not in range(60):
                print('Saida invalida...')
                continue
            #  break

            if int(h_fim) < int(h_ini):
                print('Hora da saida nao pode ser menor que a entrada...')
                continue
            break
        except:
            print('hora invalida...')
            continue

    # tratando as horas
    inicio_dt = time(int(h_ini), int(m_ini)).strftime('%H:%M')
    fim_dt = time(int(h_fim), int(m_fim)).strftime('%H:%M')
    entrada = datetime.strptime(inicio_dt, '%H:%M')
    saida = datetime.strptime(fim_dt, '%H:%M')
    horas = saida-entrada
    site = input('Local do trabalho: ') or 'Unknown'
    dias[int(dia_escolhido)-1] = [atual[0],
                                  inicio_dt, fim_dt, str(horas), site]
    mostrar_lista()
    salvar_dados(dias, CAMINHO_ARQUIVO)

###########################################


if __name__ == '__main__':

    settings = carregar_dados_arquivo([], CAMINHO_ARQUIVO_SETTINGS)
    dias = carregar_dados_arquivo([], CAMINHO_ARQUIVO)
    mostrar_lista()

    while True:
        if len(dias) == 0:
            criar_periodo()
            if incluir_horas() == 'sair':
                break
        else:
            if incluir_horas() == 'sair':
                break
