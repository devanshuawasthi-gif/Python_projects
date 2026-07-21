#  --> RULE BASED CHATBOT -->#


import datetime
import time

name = input("Welcome, Please enter you good name :")
presentHour = datetime.datetime.now().hour

if 5 <= presentHour <= 11:
    print("Good Morning", name)
elif 11 <= presentHour  <= 17:
    print("Good afternoon,", name)
elif 17 <= presentHour <= 20:
    print("Good evening", name)
else:
    print("Good night", name)



print("NAMASTE! WELCOME")
print("you can ask me basic questions , type 'bye to exit from the bot")

#-- Chatbot memory creation --> 
#--[Dictonary of responces]

responses = {
    "hello": "HI, welcome how can i help you?",
    "how are you": " I am very fine",
    "who are you": "I am smart chatbot",
    "motivate me": "Keep going. Every bug makes you a better developer",
    "happy": "Great to hear that",
}

#method / function to get responce

def getResponseOfBot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]
        
    return  "Server Error"

#--> user input
while True:
    userInput = input("please ask your question:")
    reply =getResponseOfBot(userInput)
    print("Bot response :" , reply)

    if "bye" in userInput.lower():
        break