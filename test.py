import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = os.environ.get("OPENAI_API_KEY")

def gpt3(stext):

    response = openai.Completion.create(engine="davinci-instruct-beta", prompt=stext, max_tokens=1000)

    return response.choices[0].text

query = 'What are your views on Existentialism?'

response = gpt3(query)

with open("GPT35.txt","a") as f:
    f.write(query)
    f.write(response)
   


print(response)