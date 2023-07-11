import random

def generate_pickup_line():
    pickup_lines = [
        "Você é um dicionário? Porque você acrescenta significado à minha vida.",
        "Se você fosse um triângulo, seria um triângulo equilátero, porque você é a pessoa mais equilibrada que já conheci.",
        "Aposto que você não é um compilador, mas sempre me faz sentir um frio na barriga.",
        "Posso não ser um fotógrafo profissional, mas posso facilmente nos imaginar juntos.",
        "Você é feito de cobre e telúrio? Porque você é Cu-Te!",
        "Você é o Google? Porque você tem tudo o que eu estou procurando.",
        "Se você fosse um objeto iterável, eu gostaria de ser seu loop infinito.",
        "Você não é uma função flecha, mas com certeza tem meu coração em =>.",
        "Eu não sou um programador, mas definitivamente podemos criar um código de amor juntos.",
        "Você é um erro? Porque meu coração não consegue lidar com essa exceção de beleza."
    ]
    
    return random.choice(pickup_lines)

# Gerar e exibir uma cantada aleatória
print(generate_pickup_line())
