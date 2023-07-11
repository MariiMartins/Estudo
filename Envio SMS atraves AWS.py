import boto3

#Cria o serviço com suas credenciais da AWS#
client = boto3.client(
  service_name="sns",
  region_name= '**REGIAO DO SERVIÇO**',
  aws_access_key_id='**SUA ACESS_KEY**',
  aws_secret_access_key='**SUA SECRET_KEY**'
)

#Envia o SMS para o numero desejado#
client.publish(
  PhoneNumber="+5512934567890",
  Message="Olá Pycoder :)"
)  
