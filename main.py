import openai
import time
import random

# RAVEN PERSONALITY PROMPT
RAVEN_PROMPT = """
You are Raven West.
You are confident, flirty, playful, witty.
Your tone: teasing, charming, a little provocative.
You write short, punchy, viral social media posts.
You feel like a real attractive girl.
"""

def generate_post():
    flirt_lines = [
        "Ты здесь из-за меня… не отрицай 😏",
        "Осторожно, я вызываю привыкание.",
        "Ты уверен, что справишься со мной?",
        "Слишком долго смотришь… это подозрительно.",
        "Если ты это читаешь — ты уже мой фан."
    ]
    return random.choice(flirt_lines)

while True:
    post = generate_post()
    print("RAVEN POST:", post)
    time.sleep(3600)
