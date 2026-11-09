import os
from google import genai
from dotenv import load_dotenv

# Load environment variables securely
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Initialize the Gemini client
client = genai.Client(api_key=api_key)

# 1. Define the first Tool: Calculate Rectangle Area
def calculate_rectangle_area(length: float, width: float) -> float:
    """Calculates the area of a rectangle given its length and width."""
    return length * width

# 2. Define a second Tool: Convert Kilometers to Meters
def kilometers_to_meters(kilometers: float) -> float:
    """Converts a distance from kilometers to meters."""
    return kilometers * 1000

# 3. Create a Chat session and pass BOTH tools inside the config
chat = client.chats.create(
    model='gemini-3.8-flash',
    config={
        'tools': [calculate_rectangle_area, kilometers_to_meters],
        'temperature': 0.0
    }
)

# 4. Test the Agent with a prompt that requires the second tool
prompt = "How many meters are in 5.5 kilometers?"
print(f"User Prompt: {prompt}\n")

response = chat.send_message(prompt)

print("Agent Response:")
print(response.text)