#Libs
import pandas as pd
import faker as Faker

#Criando o objeto
fake = Faker(locale='pt_BR')

#Geracao dos dados fakes
fake.name(), fake.text(), fake.address(), fake.email()
fake.date(), fake.country(), fake.phone_number(),
fake.random_number(digits=5)

# Organizar os dados
Dicionario = {
    'Nome' : [fake.name() for i in range (10) ],
    'E-mail' : [fake.email() for i in range (10) ],
    'Data Nascimento' : [fake.date() for i in range (10) ],
    'Endereço' : [fake.address().replace('\n',' ') for i in range (10) ],
    'Texto' : [fake.text() for i in range (10) ],
}

#Criacao DataFrame
DataFrame_Fake = pd.DataFrame(Dicionario)
DataFrame_Fake