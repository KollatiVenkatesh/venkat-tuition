from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_fee_reminder(student_name, month, pending_amount, language="English"):
    prompt = f"""
    Write a polite tuition fee reminder message.

    Student Name: {student_name}
    Month: {month}
    Pending Amount: {pending_amount}
    Language: {language}

    Tone: polite, respectful, short
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text
