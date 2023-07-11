import random

def generate_pickup_line(name):
    pickup_lines = [
        f"{name}, você não é uma lan house, mas desperta meu interesse gamer.",
        f"{name}, você não é um dicionário, mas é a definição de beleza.",
        f"{name}, você não é o Google, mas é tudo que eu procuro.",
        f"{name}, se beleza fosse crime, você estaria cumprindo prisão perpétua.",
        f"{name}, eu não sou um cartão de memória, mas tenho muito espaço para você no meu coração.",
        f"{name}, eu não sou fotógrafo, mas posso facilmente nos imaginar juntos em um álbum de amor.",
        f"{name}, você é uma estrela? Porque ilumina a minha vida.",
        f"{name}, você não é uma função flecha, mas com certeza tem o meu coração em =>.",
        f"{name}, você não é o Wi-Fi, mas sinto uma conexão forte entre nós.",
        f"{name}, você não é a Lua, mas é a razão do meu eclipse de coração."
    ]

    return random.choice(pickup_lines)

# Solicitar o nome do usuário
name = input("Digite o seu nome: ")

# Gerar e exibir a cantada personalizada
pickup_line = generate_pickup_line(name)
print(pickup_line)
