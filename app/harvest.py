from openai import OpenAI
from app.config import OPENAI_API_KEY
from app.crud import save_insight

def extract_insight(raw_text, source="unknown"):
    client = OpenAI(api_key=OPENAI_API_KEY)
    prompt = f"Extract structured, actionable insight from the following chaos:\n{raw_text}"
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    result = response.choices[0].message.content
    save_insight(source, result)
    return result