import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = os.environ.get("OPENAI_API_KEY")

def gpt3(stext):

    response = openai.Completion.create(engine="davinci", prompt=stext, max_tokens=1000, temperature=0.34, 
    frequency_penalty=0.31, presence_penalty=0.23, top_p=0.5)

    return response.choices[0].text

query = 'What are your views on the Anthropocene epoch?'

response = gpt3(query)

with open("GPT36.txt","a") as f:
    f.write(query)
    f.write(response)
   


print(response)