import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def load_prompt():
    with open("story_prompt.txt", "r", encoding="utf-8") as f:
        return f.read()

def generate_story(user_prompt):
    full_prompt = load_prompt() + f"\n\nUser: {user_prompt}\nAI:"
    response = openai.Completion.create(
        engine="text-davinci-003",  # μπορείς να βάλεις και gpt-3.5-turbo μέσω Chat API
        prompt=full_prompt,
        max_tokens=800,
        temperature=0.9,
        stop=["User:"]
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    print("🎙️ Καλωσήρθες στο Story AI σου!")
    user_prompt = input("Δώσε την αρχή της ιστορίας ή θέμα: ")
    story = generate_story(user_prompt)
    print("\n📖 Η ιστορία σου:\n")
    print(story)
