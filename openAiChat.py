from openai import OpenAI;

client = OpenAI(
    api_key='your-api-key'
)
def chatWithGPT(command):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a person  who speaks Bengali as well as english. You are from India and you are a chode. You analyze chat and respond like Naruto. Output should be the next chat response."},
            {
                "role": "user",
                "content": command
            }
        ]
    )
    return completion.choices[0].message.content



