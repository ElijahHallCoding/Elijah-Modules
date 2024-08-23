# This is the main module for the mood responses

# Import the custom module mood_responeses

import mood_responses

# User input
mood = input("How are you feeling today? ")

# Grab response from mood_response module
response = mood_responses.mood_response(mood)
print(response)
