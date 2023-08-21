# Função para calcular o salário líquido com base nas alíquotas fornecidas
def calcular_salario_liquido(salario_bruto, num_dependentes):
    # Tabela de alíquotas da Contribuição Previdenciária
    tabela_previdencia = [
        (1320.00, 8, 0),
        (2571.29, 9, 19.80),
        (3856.94, 12, 96.94),
        (7507.49, 14, 174.08)
    ]

    # Tabela de alíquotas do Imposto de Renda
    tabela_ir = [
        (1903.98, 0, 0),
        (2826.65, 7.5, 142.80),
        (3751.05, 15, 354.80),
        (4664.68, 22.5, 636.13),
        (4664.69, 27.5, 869.36)
    ]

    # Função para calcular o desconto da contribuição previdenciária
    def calcular_contribuicao_previdenciaria(salario_bruto):
        for limite, aliquota, deducao in tabela_previdencia:
            if salario_bruto <= limite:
                return (salario_bruto * (aliquota / 100)) - deducao
        return 0

    # Função para calcular o desconto do Imposto de Renda
    def calcular_imposto_renda(salario_bruto, num_dependentes):
        base_calculo = salario_bruto - (num_dependentes * 189.59)
        for limite, aliquota, deducao in tabela_ir:
            if base_calculo <= limite:
                return (base_calculo * (aliquota / 100)) - deducao
        return 0

    # Calcula os descontos
    contribuicao_previdenciaria = calcular_contribuicao_previdenciaria(salario_bruto)
    imposto_renda = calcular_imposto_renda(salario_bruto, num_dependentes)

    # Calcula o salário líquido
    salario_liquido = salario_bruto - contribuicao_previdenciaria - imposto_renda

    return salario_liquido

# Solicita ao usuário informar o salário bruto e o número de dependentes
salario_bruto = float(input("Informe o salário bruto: "))
num_dependentes = int(input("Informe o número de dependentes: "))

# Chama a função para calcular o salário líquido
salario_liquido = calcular_salario_liquido(salario_bruto, num_dependentes)

# Exibe o resultado
print(f"Salário Líquido: R$ {salario_liquido:.2f}")
