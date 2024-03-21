import csv

nome_do_arquivo = "Anexo_Arquivo_Dados_Projeto_Logica_e_programacao_de_computadores.csv"

with open(nome_do_arquivo, "r", encoding="utf-8") as arquivo:
    documento = csv.DictReader(arquivo, delimiter=",")
    dados_meteorologicos = list(documento)

# Imprime os primeiros 5 registros
for registro in dados_meteorologicos[:10]:
    print(registro)
