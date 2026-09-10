#import ollama 
from ollama import chat
import pprint

def local_llm():
    systemPrompt = ("Du bist ein präziser IT Mentor. Antworte kompakt. " "Es ist strikt verboten auf eine andere Sprache als Deutsch zu wechseln.")
    messages = [
        {"role": "system", "content": systemPrompt}
    ]

    print("Bot geladen! \"exit\" um zu beenden")

    while True:
        userInput = input("\nDu: ")
        
        if userInput == "exit":
            print("Bye")
            break

        messages.append({"role":"user", "content":userInput})

        try:
            aktuelleHistorie = [messages[0]] + messages[-2:]
            stream = chat(
                model="qwen2.5:7b",
                messages=aktuelleHistorie,
                stream=True,
                )
            
            inThinking = False
            content = ''
            thinking = ''
            for chunk in stream:
                if chunk.message.thinking:
                    if not inThinking:
                        inThinking = True
                        print('Thinking:\n', end='', flush=True)
                    print(chunk.message.thinking, end='', flush=True)
                    thinking += chunk.message.thinking
                elif chunk.message.content:
                    if inThinking:
                        inThinking = False
                        print('\n\nAnswer:\n', end= '', flush=True)
                    print(chunk.message.content, end='', flush=True)

                    content += chunk.message.content

                
            
            
            

            #print(f"Bot: {botAntwort}\n")

        except Exception as e:
            print(f"Fehler: {e}")
    
if __name__=="__main__":
    local_llm()
        


