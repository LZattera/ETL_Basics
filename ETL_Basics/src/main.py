import os
#o glob serve para ler aqruqivos em massa
import glob

import pandas as pd
import openpyxl as open

#caminho para ler os arquivos
input_folder_path = 'data\\raw'
#caminho para guardar o resultado
output_folder_path = 'data\\ready'
#vai listar todos os arquivo que estão no caminho informado com a extenção xlsx
excel_files = glob.glob(os.path.join(input_folder_path, '*.xlsx'))

if not excel_files:
    print('Nenhum arquivo encontrado')
else:
    #matriz na memoria com linhas e colunas para poder manipular os dados
    dfs = []

    for excel_file in excel_files:
        try:
            #Ler o arquivo de excel
            df_temp = pd.read_excel(excel_file)
            #Recuperar o nome do pais usando o nome do arquivo
            file_name = os.path.basename(excel_file)
            #Add a rastreabilidade do dado
            if 'brasil' in file_name.lower():
                #cria uma nova coluna Location
                df_temp['location'] = 'br'
            elif 'france' in file_name.lower():
                df_temp['location'] = 'fr'
            else:
                df_temp['location'] = 'it'

            #Nova coluna CAMPAING
            df_temp['campaing'] = df_temp['utm_link'].str.extract(r'utm_campaign=(.*)')

            #add coluna com nome do arquivo
            df_temp['filname'] = file_name

            #guarda os dados tratados
            dfs.append(df_temp)
            #print(df_temp)
            print(dfs)
        except Exception as ex:
            print(f'Erro ao ler o arquivo {excel_file}, \n erro: {ex}')
if dfs:
    #garante que esse processo fique em uma tabela
    result = pd.concat(dfs, ignore_index=True)

    #caminho de saida
    output_file = os.path.join('data','ready', 'clean.xlsx')

    #configura o motor de escrita
    writer = pd.ExcelWriter(output_file, engine='xlsxwriter')

    #leva os dados de resultado a serem descritos no motor de excel  configurado
    result.to_excel(writer, index=False)

    #salvar arquivo
    writer._save()
else:
    print('nenhum dado a ser salvo')