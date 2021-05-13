import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = os.environ.get("OPENAI_API_KEY")

def gpt3(stext):

    response = openai.Completion.create(engine="davinci", prompt=stext, max_tokens=1000, temperature=0.58, 
    frequency_penalty=0.39, presence_penalty=0.32, top_p=1)

    return response.choices[0].text

query = 'What is the meaning of life?'

response = gpt3(query)

with open("GPT37.txt","a") as f:
    f.write(query)
    f.write(response)
   


print(response)
