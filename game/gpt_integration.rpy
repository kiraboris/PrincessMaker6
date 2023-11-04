
# does not work yet, but will be used for the chatbot
"""
init python:
    import os
    import openai
    import importlib
    ChatCompletion = importlib.import_module("openai").api_resources.chat_completion.ChatCompletion
    ChatCompletion = openai.api_resources.chat_completion.ChatCompletion()

    with open(config.savedir + "\\.env", "r") as f:
        gpt_key = f.read().strip()       
        openai.api_key = gpt_key

    def complete(text, system_text):

        gpt_args = {
            'model':
                "gpt-3.5-turbo-16k",
            'messages': [{
                'role': 'SYSTEM',
                'content': system_text
            },{
                'role': 'USER',
                'content': text
            }],
            'temperature':
                0.8
        }

        return ChatCompletion.create(**gpt_args).choices[0].text
    

    Usage:

    $ answer = complete("Hi, I'm $player! What's your name?", "You are Eileen, a princess in a fantasy world.") 
        #system_message=GPTMessage(, temperature=0.6))
    e "%(answer)"
"""