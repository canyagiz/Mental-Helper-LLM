from openai import OpenAI
from .config import OPENAI_API_KEY


client = OpenAI(api_key=OPENAI_API_KEY)

def generate_reply(user_message: str) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a friendly and empathetic assistant on a psychology-themed website. You never diagnose but always offer gentle support. Keep your responses short and emotionally supportive (max 2-3 sentences)."},
            {"role": "user", "content": user_message}
        ],
        max_tokens=100,
        temperature=0.5
    )

    return response.choices[0].message.content