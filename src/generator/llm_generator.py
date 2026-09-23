from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"  # mindegy mit írsz, az LM Studio nem ellenőrzi
)

def generate_code(task_description: str) -> str:
    prompt = f"""Írj egy tiszta Python függvényt a következő feladatra.
Csak a kódot add vissza, semmi magyarázatot, semmi markdown-t.

Feladat:
{task_description}
"""

    response = client.chat.completions.create(
        model="qwen2.5-coder-7b-instruct",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
        max_tokens=500,
    )

    code = response.choices[0].message.content.strip()
    
    # Egyszerű tisztítás, ha véletlenül markdown-t ad
    if code.startswith("```"):
        code = code.split("```")[1]
        if code.startswith("python"):
            code = code[6:]
    code = code.strip()

    return code