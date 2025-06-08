import nltk
from nltk.stem import WordNetLemmatizer
import random

nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

intents = {
    "greeting": {
        "patterns": ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"],
        "responses": ["Hello!", "Hi there!", "Hey! How can I help you today?"]
    },
    "goodbye": {
        "patterns": ["bye", "goodbye", "see you", "later", "farewell"],
        "responses": ["Goodbye!", "See you later!", "Take care!"]
    },
    "thanks": {
        "patterns": ["thanks", "thank you", "thanks a lot", "thank you so much"],
        "responses": ["You're welcome!", "No problem!", "Happy to help!"]
    },
    "how_are_you": {
        "patterns": ["how are you", "how's it going", "how do you do", "what's up"],
        "responses": ["I'm a bot, but I'm doing great! How about you?", "Doing well, thanks for asking!"]
    },
    "bot_name": {
        "patterns": ["what's your name", "who are you", "your name", "who am i talking to"],
        "responses": ["I'm your friendly chatbot!", "You can call me ChatBot."]
    },
    "help": {
        "patterns": ["can you help me", "i need help", "help me", "can you assist me"],
        "responses": ["Sure, what do you need help with?", "I'm here to assist you. Please ask your question."]
    },
    "noanswer": {
        "patterns": [],
        "responses": ["Sorry, I didn't understand that.", "Can you say that differently?"]
    }
}

def preprocess(text):
    tokens = text.lower().split()
    return [lemmatizer.lemmatize(token) for token in tokens]

def classify(text):
    words = preprocess(text)
    for intent, data in intents.items():
        for pattern in data["patterns"]:
            pattern_words = preprocess(pattern)
            # Check if all words in pattern are in input words
            if all(word in words for word in pattern_words):
                return intent
    return "noanswer"

def get_response(intent):
    return random.choice(intents[intent]["responses"])

print("ChatBot: Hi! Type something (or 'quit' to stop)")

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("ChatBot: Goodbye! Have a great day.")
        break
    intent = classify(user_input)
    response = get_response(intent)
    print("ChatBot:", response)
