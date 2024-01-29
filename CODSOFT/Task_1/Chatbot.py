import datetime
import random

# Predefined chatbot responses
greetings = ['hello', 'hi', 'hey', 'greetings']
weather_questions = ['weather', 'temperature', 'forecast']
time_questions = ['time', 'hour', 'minute']
farewells = ['bye', 'goodbye', 'see you']

def chatbot_response(user_input):
    # Convert user input to lowercase for case-insensitive comparison
    user_input = user_input.lower()

    # Check if the user input contains any of the predefined greetings
    if any(greeting in user_input for greeting in greetings):
        return 'HEY!! I am Utkarsha,How may I help you?'
    
    # Check if the user input contains any weather-related keywords
    elif any(weather_question in user_input for weather_question in weather_questions):
        return 'The weather today is sunny.'
    
    # Check if the user input contains any time-related keywords
    elif any(time_question in user_input for time_question in time_questions):
        return f'The current time is {datetime.datetime.now().strftime("%I:%M %p")}.'
    
    # Check if the user input contains any farewell keywords
    elif any(farewell in user_input for farewell in farewells):
        return 'Bye, will meet you next time or never!'
    
    # Check if the user input contains the keyword 'joke'
    elif 'joke' in user_input:
        return random.choice([
            'Why did the programmer go broke? Because he spent all his cache on jokes and failed exams.'
        ])
    
    # Default response if none of the predefined rules match
    else:
        return 'Sorry, I didn\'t understand your query. Please try again.'

# Main loop for user interaction
while True:
    user_input = input("User: ")
    
    # Check if the user wants to exit the chat
    if user_input.lower() == 'exit':
        break
    
    # Get and print the chatbot's response
    print("Chatbot: ", chatbot_response(user_input))