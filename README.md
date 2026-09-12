# local-llm-lab

kleine skripte zum ki/llm grundlagen lernen, alles lokal mit ollama (kein api key nötig).

## setup

1. [ollama](https://ollama.com) installieren
2. modelle pullen:
   ```
   ollama pull qwen2.5:7b
   ollama pull nomic-embed-text
   ollama pull llava
   ```
3. dependencies installieren:
   ```
   pip install -r requirements.txt
   ```

## rag/

- `basicAPIUse.py` – einfachster chat-call an ein lokales modell
- `embedding.py` – text in einen vektor umwandeln (embeddings)
- `cosineSimilarity.py` – wie ähnlich sind zwei texte, mit cosine similarity gemessen
- `firstChain.py` – erste langchain pipeline (prompt -> modell -> parser), mit streaming
- `interactiveCLI.py` – chat loop mit conversation history
- `fullRAG.py` – komplettes RAG beispiel: text in chunks teilen, embedden, in chromadb speichern, bei einer frage den passenden chunk suchen und dem modell als kontext geben

am besten in der reihenfolge oben lesen, baut so ungefähr aufeinander auf.

## vision/

- `scanImage.py` – chat loop mit einem vision-modell (llava): bild per pfad einbinden, dann fragen dazu stellen

## bekannte einschränkungen

- `fullRAG.py` holt sich nur den einen ähnlichsten chunk (n_results=1), kein reranking
- history in `interactiveCLI.py` wird nicht gespeichert (geht nach dem beenden verloren)
- alles auf deutsche prompts ausgelegt, nicht getestet mit anderen sprachen
- `vision/scanImage.py` hat noch ein paar offene stellen (auskommentierter code, ein debug-print)
