import os
import requests
from dotenv import load_dotenv
from langchain.memory import ConversationBufferMemory



load_dotenv()


OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = "gpt-4o-mini"
LANG_MODEL_ENDPOINT = "https://openrouter.ai/api/v1/chat/completions"

memory = ConversationBufferMemory()

def generate_reply(prompt, lang):
    """
    Sends the user query to OpenRouter (GPT-4o-mini) and returns AI response.
    """
    context = memory.load_memory_variables({}).get("history", "")
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    system_prompt = (
        f"You are Riverwood AI, a friendly Indian voice assistant. "
        f"Always respond in {'Hindi' if lang == 'hi' else 'English'} only. "
        f"(Hindi if 'hi', English if 'en'). "
        f"Respond like a helpful companion — about weather, daily life, or construction updates — "
        f"only when the user asks for them. Be conversational and concise."
    )



    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": context + "\n" + prompt},
        ],
        "temperature": 0.8,
        "max_tokens": 150
    }

    print("Sending request to OpenRouter...")

    response = requests.post(LANG_MODEL_ENDPOINT, headers=headers, json=data, timeout=20)
    response.raise_for_status()

    response_json = response.json()
    reply = response_json["choices"][0]["message"]["content"]

    
    memory.chat_memory.add_user_message(prompt)
    memory.chat_memory.add_ai_message(reply)

   
    with open("conversation_log.txt", "a", encoding="utf-8") as f:
        f.write(f"User: {prompt}\nAI: {reply}\n\n")

    print(f"Riverwood: {reply}")
    return reply