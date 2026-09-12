import ollama
import pprint

images = []

def appendImage(path):
    images.append(path)

def local_llm():
    systemPrompt = ("describe the content of the image")
    messages = [
        {"role": "system", "content": systemPrompt}
    ]

    #print("Bot geladen! \"exit\" um zu beenden")

    while True:
        userInput = input("\nDu: ")
        
        if userInput == "exit":
            print("Bye")
            break

        if userInput == "image":
            try:
                appendImage(input("specify image name including file extension (.jpg, .png etc.) \n filepath: "))
                #messages.append({"role":"user", "content":"this image is context", "images":images.copy()})
                #del images[:]
            except Exception as e:
                        print(f"Fehler: {e}")
        else:
            messages.append({"role":"user", "content":userInput, "images":images.copy()})

            try:
                aktuelleHistorie = [messages[0]] + messages[-5:]
                print([m.get("images") for m in aktuelleHistorie])
                response = ollama.chat(
                            model="llava",
                            messages=aktuelleHistorie
                        )
                aktuelleHistorie.append(response['message'])
                print(response['message']['content'])
                

            except Exception as e:
                print(f"Fehler: {e}")
    
if __name__=="__main__":
    local_llm()
        


