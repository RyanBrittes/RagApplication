import ollama
from ragApp import RagApp

#Loop criado para interagir de maneira contínua com a LLM
while True:
    looping = input("Se desejar fazer uma pergunta digite sim, porém se quiser sair digite qualquer coisa:\n")

    if looping != "sim":
        break
    else:
        recovery = RagApp()
        question = input("Digite sua pergunta: ")
        persona = input("Digite a persona: ")

        prompt = f"""Responda com base nos seguintes documentos:
            {recovery.compair_vector(question)}

            Pergunta: {question}
            """

        response = ollama.chat(
            model="gemma3:1b",
            messages=[
                {"role": "system", "content": persona},
                {"role": "user", "content": prompt}
            ]
        )

        print("***\n" + response['message']['content'] + "\n***")
        