def calcular_salario_liquido(salario_bruto):
    # Cálculo do desconto do INSS
    if salario_bruto <= 1045.00:
        desconto_inss = salario_bruto * 0.075
    elif salario_bruto <= 2089.60:
        desconto_inss = salario_bruto * 0.09
    elif salario_bruto <= 3134.40:
        desconto_inss = salario_bruto * 0.12
    elif salario_bruto <= 6101.06:
        desconto_inss = salario_bruto * 0.14
    else:
        desconto_inss = 6101.06 * 0.14  # Para salários acima de 6101.06, o desconto é fixo

    # Cálculo do salário após o desconto do INSS
    salario_apos_inss = salario_bruto - desconto_inss

    # Cálculo do desconto do IRRF
    if salario_apos_inss <= 1903.98:
        desconto_irrf = 0
    elif salario_apos_inss <= 2826.65:
        desconto_irrf = (salario_apos_inss - 1903.98) * 0.075 - 142.80
    elif salario_apos_inss <= 3751.05:
        desconto_irrf = (salario_apos_inss - 2826.65) * 0.15 + 354.80
    elif salario_apos_inss <= 4664.68:
        desconto_irrf = (salario_apos_inss - 3751.05) * 0.225 + 636.13
    else:
        desconto_irrf = (salario_apos_inss - 4664.68) * 0.275 + 869.36

    # Cálculo do salário líquido final
    salario_liquido = salario_apos_inss - desconto_irrf

    return salario_liquido

# Solicitar entrada do usuário
salario_bruto = float(input("Digite o salário bruto: "))

# Calcular e exibir o salário líquido
salario_liquido = calcular_salario_liquido(salario_bruto)
print(f"O salário líquido é: {salario_liquido:.2f}")
