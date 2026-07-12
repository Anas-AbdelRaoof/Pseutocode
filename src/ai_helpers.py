from sys import exit
try:
    from groq import Groq, APIConnectionError, APIStatusError, APITimeoutError, RateLimitError
    from dotenv import load_dotenv
    from rich import print
except ModuleNotFoundError:
    print("Please download requirements.txt by <pip install -r requirements.txt --break-system-packages>")
    exit()
import os
from system_prompt import system_prompt


def convert_pseudocode_to_code_with_ai():
    """
    Connect to Groq API and convert pseudocode to actual code using AI.
    
    This function sends pseudocode to the Groq API (using the Llama 3.3 70B model)
    and returns the AI-generated code based on the system prompt.
    
    Returns:
        str: The AI-generated code as a string
    """

    # Load environment variables from .env file to access API credentials securely
    load_dotenv()

    # Initialize the Groq API client with the API key from environment variables
    try:
        client = Groq(
            api_key=os.environ.get("GROQ_API_KEY")
        )
    except APIConnectionError as e:
        print(f"[red]Failed to connect to Groq API:[/red] [italic blue]{e}[/italic blue]")
        exit()
    except APIStatusError as e:
        print(f"[red]Groq API returned an error status:[/red] [italic blue]{e}[/italic blue]")
        exit()
    except APITimeoutError as e:
        print(f"[red]Groq API request timed out:[/red] [italic blue]{e}[/italic blue]")
        exit()
    except RateLimitError as e:
        print(f"[red]Groq API rate limit exceeded:[/red] [italic blue]{e}[/italic blue]")
        exit()

    # Send a chat completion request to the Groq API with the system prompt
    # The model will process the pseudocode and generate corresponding code
    current_system_prompt = system_prompt()

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": current_system_prompt,
                } # The system prompt alows AI to convert pseudocode nto programming languages
            ],
            model="llama-3.3-70b-versatile",
        )
    except APIConnectionError as e:
        print(f"[red]Failed to connect to Groq API:[/red] [italic blue]{e}[/italic blue]")
        exit()
    except APIStatusError as e:
        print(f"[red]Groq API returned an error status:[/red] [italic blue]{e}[/italic blue]")
        exit()
    except APITimeoutError as e:
        print(f"[red]Groq API request timed out:[/red] [italic blue]{e}[/italic blue]")
        exit()
    except RateLimitError as e:
        print(f"[red]Groq API rate limit exceeded:[/red] [italic blue]{e}[/italic blue]")
        exit()

    # Extract and return the generated code from the API response
    return chat_completion.choices[0].message.content
