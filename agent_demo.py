import os
from google import genai
from dotenv import load_dotenv

# Load environment variables securely
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Initialize the Gemini client
client = genai.Client(api_key=api_key)

# 1. Define a Python function (Tool) that the Agent can use
def calculate_rectangle_area(length: float, width: float) -> float:
    """Calculates the area of a rectangle given its length and width."""
    return length * width

# 2. Create a Chat session and pass the tool inside the config
chat = client.chats.create(
    model='gemini-3.8-flash',
    config={
        'tools': [calculate_rectangle_area],
        'temperature': 0.0
    }
)

# 3. Send the message through the chat session (Recommended for AFC)
prompt = "Can you calculate the area of a rectangle with a length of 15.5 and a width of 4.2?"
print(f"User Prompt: {prompt}\n")

response = chat.send_message(prompt)

print("Agent Response:")
print(response.text)