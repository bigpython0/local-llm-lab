from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def main():
    model = ChatOllama(
        model="qwen2.5:7b",
        temperature=0.7 
    )

    #dynamic template
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "Du bist ein lustiger Informatik-Professor. Antworte kurz."),
        ("user", "Erzähl mir einen kurzen Witz über das Thema: {thema}")
    ])

    #llm antwort -> normal text
    output_parser = StrOutputParser()

    # pipeline mit "|"
    chain = prompt_template | model | output_parser

    userInput = input("Worüber willst du einen Witz hören?\n")
    
    print("Bot-Antwort:")

    # statt antwort = chain.invoke(...)
    for chunk in chain.stream({"thema": userInput}):
        print(chunk, end="", flush=True)
    
    
    #print(antwort)

if __name__ == "__main__":
    main()