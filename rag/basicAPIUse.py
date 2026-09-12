import ollama
import pprint

def chat_mit_lokalem_llm():
    # verlauf, brauch ich für memory in woche 3
    messages = [
        {
            "role": "system",
            "content": "Du bist ein erfahrener Senior-Entwickler. Antworte präzise, professionell und auf Deutsch."
        },
        {
            "role": "user",
            "content": "was ist der unterschied zwischen einer liste und einem tuple in python?"
        }
    ]

    try:
        print("Generiere Antwort vom lokalen Modell...\n")
        
        # läuft lokal, kein api key nötig
        response = ollama.chat(
            model="qwen2.5:7b",  # vorher pullen nicht vergessen
            messages=messages
        )

        print("--- KI ANTWORT ---")
        #print(response['message']['content'])
        pprint.pprint(response)
        
    except Exception as e:
        print(f"Fehler aufgetreten: {e}")
        print("Tipp: Läuft die Ollama-App im Hintergrund?")

if __name__ == "__main__":
    chat_mit_lokalem_llm()