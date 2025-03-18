import chainlit as cl
import random
import datetime

# List of fun facts
FUN_FACTS = [
    "Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still good to eat!",
    "Octopuses have three hearts and blue blood!",
    "Bananas are berries, but strawberries aren't!",
    "Water can boil and freeze at the same time, called the 'triple point'.",
    "A day on Venus is longer than a year on Venus!"
]

# List of jokes
JOKES = [
    "Why don’t scientists trust atoms? Because they make up everything!",
    "Parallel lines have so much in common. It’s a shame they’ll never meet.",
    "Why did the computer catch a cold? Because it left its Windows open!",
    "I'm reading a book about anti-gravity. It's impossible to put down!",
    "Why don’t skeletons fight each other? They don’t have the guts!"
]

# Keyword-based response
def get_response(text):
    text = text.lower()
    if any(word in text for word in ["hi", "hello", "hey"]):
        return "Hello! 👋 How can I assist you today?"
    elif any(word in text for word in ["bye", "goodbye", "see you"]):
        return "Goodbye! Have a great day! 😊"
    elif any(word in text for word in ["how are you", "what's up"]):
        return "I'm just a bot, but I'm here to help! 🚀"
    elif "joke" in text:
        return random.choice(JOKES)
    elif "fun fact" in text:
        return random.choice(FUN_FACTS)
    else:
        return None  # Default case

@cl.on_message
async def main(message: cl.Message):
    user_text = message.content
    response_text = get_response(user_text)

    # Word count feature
    word_count = len(user_text.split())

    # Timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Generate final response
    response = f"**You said:** {user_text}\n"
    response += f"**Word Count:** {word_count} words 📖\n"
    response += f"🕒 **Timestamp:** {timestamp}\n"

    if response_text:
        response += f"\n**Response:** {response_text}"

    await cl.Message(content=response).send()



