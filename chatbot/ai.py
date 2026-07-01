from openai import OpenAI
from config import Config
from chatbot.prompts import SYSTEM_PROMPT

client = OpenAI(api_key=Config.OPENAI_API_KEY)

def get_ai_response(user_message):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role":"system","content":SYSTEM_PROMPT},
            {"role":"user","content":user_message}
        ],
        temperature=0.7,
        max_tokens=500
    )
    return response.choices[0].message.content
