import openai
openai.api_key="votre key OpenAi"
def generate_description(input):
    messages=[
        {"Role":"System",
        "Content":"""As a product description generator, generate multi paragraph rich text product description\n"""},
    ]
    messages.append({"role":"user", "content":f"{input}"})
    completion=openai.chat.completions(
        model="gpt-3.5-turbo",
        messages=messages
    )

    reply=completion.choices[0].message.content
    return reply
