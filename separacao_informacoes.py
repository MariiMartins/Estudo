import re

# Lista para armazenar as informações classificadas
informacoes_classificadas = []

# Linhas de amostra
linhas = [
    "5 MG/ML XPE CT FR VD AMB X 120 ML + COP",
    "15 MG/G CREM DERM CT BG AL X 30 G",
    "100 MG COM REV CT STR AL X 12",
    "250 MG COM CT FR PLAS PEAD OPC X 120",
    "7,5 MG/ML SOL INJ CT FA VD TRANS X 0,9 ML",
]

# Função para classificar uma linha
def classificar_linha(linha):
    # Verifica se é injetável
    if "INJ" in linha:
        injetavel = "Sim"
    else:
        injetavel = "Não"
    
    # Extrai a quantidade de MG
    mg = re.search(r'(\d+(\.\d+)?)\s*MG', linha)
    if mg:
        mg = mg.group(1)
    else:
        mg = "Não especificado"
    
    # Determina o tipo de medicamento
    if "CREM" in linha:
        tipo = "Creme"
    elif "XPE" in linha:
        tipo = "Xarope"
    elif "COM REV" in linha:
        tipo = "Comprimido Revestido"
    elif "COM" in linha:
        tipo = "Comprimido"
    elif "SOL INJ" in linha:
        tipo = "Solução Injetável"
    else:
        tipo = "Não especificado"
    
    # Extrai a posologia
    posologia = re.search(r'X\s*(\d+(\.\d+)?)\s*(\w+)', linha)
    if posologia:
        posologia = f"{posologia.group(1)} {posologia.group(3)}"
    else:
        posologia = "Não especificado"
    
    # Armazena as informações classificadas
    informacoes_classificadas.append({
        "MG": mg,
        "Tipo": tipo,
        "Injetável": injetavel,
        "Posologia": posologia,
    })

# Processa cada linha e classifica as informações
for linha in linhas:
    classificar_linha(linha)

# Imprime as informações classificadas
for i, info in enumerate(informacoes_classificadas, start=1):
    print(f"Informações da Linha {i}:")
    print(f" - MG: {info['MG']}")
    print(f" - Tipo: {info['Tipo']}")
    print(f" - Injetável: {info['Injetável']}")
    print(f" - Posologia: {info['Posologia']}")
    print()
