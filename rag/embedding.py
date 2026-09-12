import ollama

def embedding_demo():
    text1 = "Python ist eine tolle Programmiersprache für KI."
    text2 = "Ich liebe es, Code mit Java zu schreiben."
    text3 = "Heute ist das Wetter draußen ziemlich bewölkt."

    response = ollama.embeddings(model="nomic-embed-text", prompt=text1) 
    vector = response['embedding'] #holt sich nur das embedding

    print(f"Text: '{text1}'")
    print(f"Länge des Vektors (Dimensionen): {len(vector)}")
    print(f"Die ersten 5 Zahlen des Vektors: {vector[:5]}...")

if __name__ == "__main__":
    embedding_demo()