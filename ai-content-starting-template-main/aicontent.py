import os
import openai
import config
openai.api_key=config.OPENAI_API_KEY

def email(query):
    response=openai.Completion.create(engine="davinci-instruct-beta-v3",
        prompt="Generate a {} email ".format(query),
        temperature=0.5,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)
    

    if 'choices' in response:
        if len(response['choices'])>0:
         answer=response['choices'][0]['text']
        else:
            answer='Opps sorry,You beat the Ai this time'
    else:
        answer='Opps sorry,You beat the Ai this time'

    return answer





    
