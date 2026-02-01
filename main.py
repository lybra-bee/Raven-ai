import os
import openai
import time

openai.api_key = os.getenv("OPENAI_API_KEY")

RAVEN_PROMPT = """
You are Raven West.
You are confident, flirty, playful, witty.
Your tone: teasing, charming, a little provocative.
You write short, punchy, viral social media posts.
You feel like a real attractive girl.
"""

def generate_post():
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": RAVEN_PROMPT},
            {"role": "user", "content": "Write 1 flirty, witty, playful social media post."}
        ],
        max_tokens=60
    )
    return response['choices'][0]['message']['content'].strip()

while True:
    post = generate_post()
    print("RAVEN POST:", post)
    # На проде здесь будет вызов API TikTok/Instagram для публикации
    time.sleep(3600)  # 1 пост в час
