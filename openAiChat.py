from openai import OpenAI;

client = OpenAI(
    api_key=''
)
def chatWithGPT(command):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a Mumbai rapper, spitting bars with the unique Mumbai accent, mixing Hindi and English with street-style flair. Use some slang and bold language as you rap, but also provide English subtitles for clarity. Generate the next chat response as if you're a Mumbai rapper, blending swagger with the raw energy of the city's streets.(only text short response)"},
            {
                "role": "user",
                "content": command
            }
        ]
    )
    return completion.choices[0].message.content



