import os
import openai

# Load your API key from an environment variable or secret management service

def gpt3(stext):

    openai.api_key = os.environ.get("OPENAI_API_KEY")

    response = openai.Completion.create(engine="davinci-instruct-beta", prompt=stext, max_tokens=1000)

    return response.choices[0].text

query = 'Tell me about ABESIT College in India'

response = gpt3(query)

with open("GPT34.txt","a") as f:
    f.write(query)
    f.write(response)
   


print(response)