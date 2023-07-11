import openai

#Deine OpenAI Key
openai.api_key = "Your_API_Key"

#Set up the model and prompt
model_engine = "text-davinci-003"
prompt = input ('Enter new prompt: ')

#Generate a response
completion = onpenai.Completion.create(
  engine=model_engine,
  prompt=prompt
  max_tokens=1024,
  n=1,
  stop=None,
  temperature=0.5,
)

response = completion.choices[0].text
print(reponse)
