from openai import OpenAI
import chromadb
import ollama

def chunk_text_by_words(text, chunk_size=15, overlap=5):
    words = text.split()
    chunks = []

    i = 0
    while i < len(words):
        chunk_words = words[i : i + chunk_size] 
        chunk = " ".join(chunk_words)
        chunks.append(chunk)

        i += (chunk_size-overlap) #springt bis ende des Chunks aber gibt Raum für overlap

    return chunks

file_path= "RAG_Text.txt"

meine_chunks = []

try:
    with open(file_path, "r", encoding="utf-8") as file:
        volltext = file.read()

        meine_chunks = chunk_text_by_words(volltext, chunk_size=80, overlap=30)

        print(f"Datei eingelesen. Wortanzahl: {len(volltext.split())}")

except FileNotFoundError:
    print(f"Fehler: Datei {file_path} nicht gefunden.")
    exit()

ollama_client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

def get_embedding(text, model="nomic-embed-text"):
    response = ollama_client.embeddings.create(
        model=model,
        input=text
    )

    return response.data[0].embedding

chroma_client = chromadb.PersistentClient(path="./mein_chroma_db")
collection = chroma_client.get_or_create_collection(name="firmen_wissen")

ids = [f"doc_id_{i}" for i in range(len(meine_chunks))] # ID für jeden Chunk

print("Generiere Embeddings und füttere Datenbank...")
embeddings = [get_embedding(doc) for doc in meine_chunks] # ist einfach eine liste von floats

collection.add( # collection eine liste aus zeilen. Jede Zeile bedeutet:
    embeddings=embeddings, #embedding vektor
    documents=meine_chunks, #originaler text
    ids=ids # eindeutige ID
)
print("Daten erfolgreich gespeichert!\n")

#chat

user_frage = input("Du: ")

print(f"User-Frage: '{user_frage}")

frage_embedding = get_embedding(user_frage)

#1. retrieval
ergebnisse = collection.query(
    query_embeddings=[frage_embedding],
    n_results=1
)

gef_Dokument = ergebnisse['documents'][0][0]
print(f"Gefundener Kontext: {gef_Dokument}")



try:
    # 2. Augmentation
    system_Prompt = (
        "Du bist ein hilfreicher HR-Assistent der Firma. "
        "Beantworte die Frage des Nutzers ausschließlich auf Basis des bereitgestellten Kontextes. "
        "Wenn der Kontext die Antwort nicht hergibt, antworte mit 'Das weiß ich leider nicht.'\n\n"
        f"KONTEXT:\n{gef_Dokument}" # hier wissen 'injiziert'
) 


    #3. Generation
    response = ollama.chat(
        model="qwen2.5:7b",
        messages = [
            {"role":"system", "content":system_Prompt},
            {"role":"user", "content": user_frage}
        ]
    )

    print("Bot: ", end='')
    print(response['message']['content'])

except Exception as e:
    print(f"Fehler: {e}")