from groq import Groq
import os
from dotenv import load_dotenv
from system_prompt import system_prompt


def convert_pseudocode_to_code_with_ai():
    """
    Connect to API and allows it to read pseudocode and write/print
    """

    load_dotenv()

    # This part is from Gemini
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY")
    )

    systemPrompt = system_prompt()

    # This code is from Quickstart - GroqDocs
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": systemPrompt,
            }  # The System Prompt is from my creation
        ],
        model="llama-3.3-70b-versatile",
    )

    return chat_completion.choices[0].message.content
