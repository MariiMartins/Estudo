import subprocess

# Obter metadados
meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])

# Decodificar metadados
data = meta_data.decode('utf-8', errors="backslashreplace")

# Dividir dados linha por linha
data = data.split('\n')

# Criar uma lista de perfis
profiles = []

# Percorrer os dados
for line in data:
    # Encontrar "All User Profile" em cada item
    if "All User Profile" in line:
        line = line.split(":")[1].strip()
        profiles.append(line)

# Imprimir cabeçalho
print("{:<30}| {:<}".format("Nome do Wi-Fi", "Senha"))
print("__")

# Percorrer os perfis
for profile in profiles:
    try:
        # Obter metadados com a senha usando o nome do Wi-Fi
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'])
        results = results.decode('utf-8', errors="backslashreplace")
        results = results.split('\n')
        
        # Encontrar a senha na lista de resultados
        password = [line.split(":")[1].strip() for line in results if "Key Content" in line]
        
        if password:
            print("{:<30}| {:<}".format(profile, password[0]))
        else:
            print("{:<30}| {:<}".format(profile, ""))
    except subprocess.CalledProcessError:
        print("Ocorreu um erro de codificação")

