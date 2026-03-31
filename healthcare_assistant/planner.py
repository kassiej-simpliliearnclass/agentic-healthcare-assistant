import json
import os
from openai import OpenAI
from dotenv import load_dotenv


ALLOWED_TASKS = {"book_appointment", "search_medical_info"}


def plan_tasks(user_input: str):
    load_dotenv(override=True)
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return []

    client = OpenAI(api_key=api_key)

    prompt = f"""
You are a healthcare assistant planner.

Return ONLY valid JSON like this:
{{"tasks": ["book_appointment", "search_medical_info"]}}

Allowed task names:
- book_appointment
- search_medical_info

Rules:
- Use "book_appointment" if the user wants to book, schedule, arrange, or see a doctor
- Use "search_medical_info" if the user wants treatment info, disease info, latest info, or a summary
- Return only the allowed task names
- Do not include explanations
- Do not include markdown
- If both are needed, return both

User request:
{user_input}
"""

    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=prompt
        )
        text = response.output_text.strip()

        data = json.loads(text)
        tasks = data.get("tasks", [])

        clean_tasks = []
        for task in tasks:
            if isinstance(task, str) and task in ALLOWED_TASKS and task not in clean_tasks:
                clean_tasks.append(task)

        return clean_tasks

    except Exception:
        tasks = []
        lowered = user_input.lower()

        booking_words = ["book", "appointment", "schedule", "arrange", "doctor", "specialist", "nephrologist"]
        info_words = ["treatment", "treatments", "latest", "summarize", "summary", "options", "information"]

        if any(word in lowered for word in booking_words):
            tasks.append("book_appointment")

        if any(word in lowered for word in info_words):
            tasks.append("search_medical_info")

        return tasks