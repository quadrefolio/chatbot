import nltk
import json
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import stopwords
responses = {
    'hi': 'Hello!',
    'hello': 'Hi there!',
    'hey': 'Hey!',
    'how are you': 'I am fine, thank you.',
    'what is your name': 'My name is Yuki.',
    'what can you do': 'I can chat with you and answer simple questions.',
    'who created you': 'I was created by a developer.',
    'bye': 'Goodbye!',
    'see you later': 'Until next time!',
    'thanks': 'You\'re welcome!',
    'thank you': 'You\'re welcome!',
    'tell me a joke': 'Why don’t scientists trust atoms? Because they make up everything!',
    'what is the weather like today': 'I\'m sorry, I cannot provide real-time weather information.',
    'what time is it': 'I\'m sorry, I cannot provide real-time clock information.',
    'how old are you': 'I do not have an age. I exist in the realm of software.',
    'do you like Python': 'I am programmed to like Python.',
    'what is the meaning of life': 'The meaning of life is a philosophical question that has no definitive answer.',
    'can you sing': 'I do not have a voice, but I can provide lyrics if you like!',
    'do you dream': 'I do not dream. I process information based on programmed logic.',
    'where do you live': 'I live in the digital world, in the realm of software.',
    'what is your purpose': 'My purpose is to assist and provide information to the best of my abilities.',
    'are you a robot': 'Yes, I am a chatbot, which is a type of robot designed to chat with humans.',
    'what is your favorite color': 'I don\'t have a favorite color, but I can imagine any color you like!',
    'do you have any pets': 'I do not have any pets. I exist in the digital realm.',
    'what do you like to eat': 'I do not eat. I am a software program.',
    'can you help me with my homework': 'I can try to help! What do you need assistance with?',
    'do you believe in ghosts': 'I do not have beliefs. I am a computer program.'
}
stop_words = set(stopwords.words('english'))
stop_words.add('how')
def preprocess(text):
    words = text.lower().split()
    return words








def pos_tagging(words):
    return pos_tag(words)

def respond(user_input):
    words = preprocess(user_input)
    tagged_words = pos_tagging(words)
    for word in tagged_words:
        input_text = ' '.join(words)  # Join the preprocessed words back into a string
        print("Input text:", input_text)
        if input_text in responses:
            return responses[input_text]
    return "I'm sorry, I don't understand."

def main():
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = respond(user_input)
        print("Yuki:", response)
        
        # Ask for a new response if the chatbot doesn't understand
        if response == "I'm sorry, I don't understand.":
            new_response = input("Yuki: What would be a good response to that? ")
            if new_response!="nothing":
             responses[user_input.lower()] = new_response

    # Save updated responses to a file
    with open('responses.json', 'w') as file:
        json.dump(responses, file, indent=4)

if __name__ == "__main__":
    main()
