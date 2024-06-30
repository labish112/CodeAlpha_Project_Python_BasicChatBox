import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"fine[, ]?what about you[?]?",
        ["I'm doing well too. How can I assist you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot created by you. You can call me ChatBot!",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "It's OK, never mind",]
    ],
    [
        r"what is your favorite color ?",
        ["I don't have a favorite color. What's yours?",]
    ],
    [
        r"i like (.*) color",
        ["That's nice! Why do you like %1?",]
    ],
    [
        r"what is the weather like ?",
        ["I'm not sure, but I hope it's nice where you are!",]
    ],
    [
        r"do you like (.*)",
        ["I don't have personal preferences, but I think %1 is interesting!",]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!",]
    ],
    [
        r"who created you ?",
        ["I was created by a developer who loves to code.",]
    ],
    [
        r"what is your purpose ?",
        ["I am here to chat with you and make your day a little brighter!",]
    ],
    [
        r"can you help me with (.*)",
        ["I can try my best to help you with %1. What do you need?",]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon :)", "It was nice talking to you. See you soon :)"]
    ],
]

def chatbot():
    print("Hi! I am a simple chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
