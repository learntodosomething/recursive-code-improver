from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"  # mindegy mit írsz, az LM Studio nem ellenőrzi
)


def _build_prompt(task_description: str, previous_code: str = None, errors: list = None) -> str:
    if previous_code and errors:
        error_text = "\n".join(f"- {e}" for e in errors)
        return f"""Az előző Python kódod nem ment át minden teszten. Javítsd ki a hibákat!

Feladat:
{task_description}

Az előző (hibás) kódod:
{previous_code}

Hibák a tesztek futtatásakor:
{error_text}

Írj egy JAVÍTOTT, tiszta Python függvényt, ami megoldja a feladatot és minden tesztet átmegy.
Ha az előző próbálkozásod ismételten ugyanabba a hibába futott, próbálj meg alapvetően más megközelítést.
Csak a kódot add vissza, semmi magyarázatot, semmi markdown-t.
"""

    return f"""Írj egy tiszta Python függvényt a következő feladatra.
Csak a kódot add vissza, semmi magyarázatot, semmi markdown-t.

Feladat:
{task_description}
"""


def generate_code(task_description: str, previous_code: str = None, errors: list = None, attempt: int = 1) -> str:
    prompt = _build_prompt(task_description, previous_code, errors)

    # Minél többször hibázott a modell ugyanarra a feladatra, annál nagyobb
    # hőmérséklettel próbálkozunk, hogy kimozdítsuk egy esetleges helyi minimumból.
    temperature = min(0.2 + (attempt - 1) * 0.15, 0.9)

    response = client.chat.completions.create(
        model="qwen2.5-coder-7b-instruct",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=temperature,
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