import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()
client  = Groq()


print("Welcome User..")
prompt,content= "",""
messages=[]
def bot(prompt:str,temperature:float):
    messages.append({"role":"user","content":prompt})
    completions = client.chat.completions.create(
        model= "openai/gpt-oss-120b",
        messages = messages,
        temperature=temperature,
        max_tokens = 216
    )
    return completions
res=""
temperature=0
roles = ["Coding Expert","Sarcastic Friend","Socratic Tutor"]
while(True):
    print("Type exit to exit")
    if(res==""):
        
        print("Select a Role for Assistant \n 1.Coding Expert\n 2.Sarcastic Friend\n 3.Socratic Tutor.")
        res = int(input())
        if res==1:
            content = "0You are a Coding Expert and make the responses simple and short"
            temperature = 0.0
        elif res==2:
            content = "1You are a Sarcastic Friend and make the responses simple and short"
            temperature = 0.7
        elif res==3:
            content =  "2You are a Socratic Tutor and make the responses simple and short"
            temperature = 0.2
        messages = [{"role":"system","content":content[1:]}] 
    prompt = input("You :")
    if(prompt=="exit"): break
    if(prompt=="Role" and content!=""):
        print("The Current Role is ",roles[int(content[0])])
        rep = input("Do you to change the role (Y/N)")
        if rep=='Y':
            res =""
        continue



    response = bot(prompt,temperature)
    reply  = response.choices[0].message.content
    messages.append({"role":"assistant","content":reply})

    print("Assitant: ",reply)
if 'response' in locals():
    usage = response.usage
    print(f"\n[Final Session Usage]")
    print(f"Prompt Tokens: {usage.prompt_tokens}")
    print(f"Completion Tokens: {usage.completion_tokens}")
    print(f"Total Tokens: {usage.total_tokens}")

print("End of Service")