import re

# Lista para armazenar as informações classificadas
informacoes_classificadas = []

# Linhas de amostra
linhas = [
    "100 MG/ML SOL INJ IV/INAL CT 5 AMP VD AMB X 3 ML",
    "11,76 + 0,04 + 30 MG/ML SOL OR CT FR VD AMB CGT X 15 ML",
    "(2,5 + 1,5) MG COM REV CT BL AL PLAS PVC/PVDC TRANS CALEND X 24 + 4 PLACEBO",
    "10 MG/ML SUS OFT CT FR GOT PLAS OPC X 5 ML",
]

# Função para classificar uma linha
def classificar_linha(linha):
    # Verifica se é injetável
    if "INJ" in linha:
        injetavel = "Sim"
    else:
        injetavel = "Não"
    
    # Extrai a quantidade de MG ou UI
    mg_ui = re.search(r'(\d+(\.\d+)?)\s*(MG\/ML|MG|UI)', linha)
    if mg_ui:
        mg_ui = mg_ui.group(1) + " " + mg_ui.group(3)
    else:
        mg_ui = "Não especificado"
    
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
    elif "CAP MOLE" in linha:
        tipo = "Capsula Mole"
    elif "CAP" in linha:
        tipo = "Capsula"        
    else:
        tipo = "Não especificado"
    
    # Verifica o tipo de embalagem
    if "FR VD" in linha:
        embalagem = "Frasco de Vidro"
    elif "CX" in linha:
        embalagem = "Caixa (CX)"
    elif "FR PL" in linha:
        embalagem = "Frasco de Plastico"
    elif "AMP VD" in linha:
        embalagem = "Ampola de Vidro"    
    else:
        embalagem = "Não especificado"
    
    # Extrai a posologia
    posologia = re.search(r'X\s*(\d+(\.\d+)?)\s*(\w+)', linha)
    if posologia:
        posologia = f"{posologia.group(1)} {posologia.group(3)}"
    else:
        posologia = "Não especificado"
    
    # Armazena as informações classificadas
    informacoes_classificadas.append({
        "MG/UI": mg_ui,
        "Tipo": tipo,
        "Injetável": injetavel,
        "Embalagem": embalagem,
        "Posologia": posologia,
    })

# Processa cada linha e classifica as informações
for linha in linhas:
    classificar_linha(linha)

# Imprime as informações classificadas
for i, info in enumerate(informacoes_classificadas, start=1):
    print(f"Informações da Linha {i}:")
    print(f" - Dosagem/Concentracao: {info['MG/UI']}")
    print(f" - Tipo: {info['Tipo']}")
    print(f" - Injetável: {info['Injetável']}")
    print(f" - Embalagem: {info['Embalagem']}")
    print(f" - Posologia: {info['Posologia']}")
    print()
