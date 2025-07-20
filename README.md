# Projeto de Limpeza e Unificação de Arquivos Excel

Este projeto em Python automatiza a leitura, tratamento e consolidação de múltiplos arquivos `.xlsx` que contêm dados de campanhas de marketing digital de diferentes países.

# Estrutura de Diretórios

├── .venv/ # Ambiente virtual
├── src
| ├── data
│ | ├── raw/ # Coloque aqui os arquivos .xlsx de entrada
│ | └── ready/ # Aqui será salvo o arquivo Excel consolidado e limpo
│ └── main.py # Script principal do projeto


# Funcionalidades

- Lê múltiplos arquivos `.xlsx` da pasta `data/raw`
- Identifica a **localização geográfica** dos dados com base no nome do arquivo (`brasil`, `france` e 'italian')
- Extrai automaticamente a campanha da URL (`utm_campaign=...`)
- Adiciona rastreabilidade com o nome do arquivo de origem
- Consolida todos os dados em um único arquivo `clean.xlsx` na pasta `data/ready`

# Pré-requisitos
- Python 3 instalado
- Instalar as dependências com:
    pip install pandas openpyxl xlsxwriter
  
# Como rodar o projeto
Coloque os arquivos .xlsx que deseja processar dentro de data/raw
Execute o script:
  python src/main.py
O arquivo limpo clean.xlsx será gerado em data/ready

# Regras de processamento
location: baseada no nome do arquivo
Contém 'brasil'    → br
Contém 'france'    → fr
Qualquer 'italian' → it

campaing: extraída da coluna utm_link, pegando o valor do parâmetro utm_campaign

filname: nome do arquivo de origem adicionado como coluna

Exemplo de saída (clean.xlsx)
utm_link	                                location	  campaing	  filname
https://site.com/?utm_campaign=blackfr	  br	        blackfr	    brasil_ads.xlsx
https://site.com/?utm_campaign=verao	    fr	        verao	      france_data.xlsx

# Observações
A pasta data/ready será criada automaticamente, se não existir
Se nenhum arquivo válido for encontrado em data/raw, o script exibirá uma mensagem de aviso
Os arquivos de entrada devem conter ao menos a coluna utm_link

**Importante** No arquivo gitignore tem que descomentar a linha 10 que não sobre os arquivos da pasta raw, não se pode subir os arquivos base para nuvem ou software de versionamento pois isso causa uma falha de segurança.

# Melhorias futuras
Suporte a arquivos .csv
Validação de colunas obrigatórias
Exportação também para .csv
Logs e tratamento de exceções mais robustos

