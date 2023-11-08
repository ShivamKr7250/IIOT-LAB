from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot instance
chatbot = ChatBot('MyChatBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on English language data
trainer.train('chatterbot.corpus.english')

# Function to get the chatbot's response
def get_bot_response(user_input):
    return chatbot.get_response(user_input)

# Main loop to interact with the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response = get_bot_response(user_input)
    print("ChatBot:", response)
