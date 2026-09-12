import ollama
import numpy as np

def cosine_similarity(v1, v2):
    dot_product = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    return dot_product / (norm_v1 * norm_v2)

#embeddings generieren
model_name = "nomic-embed-text"
emb_python = ollama.embeddings(model=model_name, prompt="Python ist eine tolle Programmiersprache für KI.")['embedding']
emb_java = ollama.embeddings(model=model_name, prompt="Ich liebe es, Code mit Java zu schreiben.")['embedding']
emb_wetter = ollama.embeddings(model=model_name, prompt="Heute ist das Wetter draußen ziemlich bewölkt.")['embedding']

#ähnlichkeit Berechnen
sim_python_java = cosine_similarity(emb_python, emb_java)
sim_python_wetter = cosine_similarity(emb_python, emb_wetter)

print(f"Ähnlichkeit (Python <-> Java):   {sim_python_java:.4f}  (Nah an 1 = Ähnlich!)")
print(f"Ähnlichkeit (Python <-> Wetter): {sim_python_wetter:.4f} (Nah an 0 = Unähnlich!)")