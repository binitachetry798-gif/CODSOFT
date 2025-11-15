# Rule based chatbot

import random
import re

intents = {
    "greetings": {
        "patterns": ["hello","hi","hey","hola"],
        "responses": ["hello!","hi there!","hey!"]
    },
    "goodbyes":{
        "patterns": ["bye","goodbye","see you","later"],
        "responses": ["goodbye!","see you later!","take care!"]
    },
    "thanks":{
        "patterns": ["thanks","thank you","appreciate it"],
        "responses": ["you're welcome!","no problem!","happy to help!","anytime!"]
    },
    "questions":{
        "how are you": ["I'm fine,thank you!","doing great,what about you?"],
        "what's your name": ["I'm a simple rule based chatbot.What's your name?"],
        "what can you do": ["I can chat with you!"]
    }
}

def match_intent(user_input):
    for intent, intent_data in intents.items():
        if isinstance(intent_data, dict) and "patterns" in intent_data:
            for pattern in intent_data["patterns"]:
                if re.search(pattern, user_input, re.IGNORECASE):
                    return random.choice(intent_data["responses"])
                
    for question, responses in intents["questions"].items():
        if question in user_input.lower():
            return random.choice(responses)
        
    return None

def get_response(user_input):
    matched_intent = match_intent(user_input)

    if matched_intent:
        return matched_intent
    else:
        return "I didn't quite understand that, could you please try asking something else?"
    
def chatbot():
        print("Chatbot: Hi!, I'm a simple rule based chatbot.How can i assist you today?")

        while True:
            user_input = input("You: ")

            if "bye" in user_input.lower():
                print("Chatbot: Goodbye!")
                break

            response = get_response(user_input)
            print("Chatbot:",response)

chatbot()