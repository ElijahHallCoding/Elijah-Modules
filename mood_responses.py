# Python Modules and Data Handling Assignment

# Task 1: Your Mood Today

# Get Mood Response
def mood_response(mood):

    #Convert mood to lowercase
    mood = mood.lower()

    # Mood Responses
    if mood == "happy":
        return "That's great to hear! Keep smiling!"
    elif mood == "sad":
        return "I'm sorry to hear that. I hope things get better soon."
    elif mood == "excited":
        return "Wow, that's awesome! Keep that energy going! It's electric!"
    elif mood == "angry":
        return "Take a ddep breath. It's okay to feel angry sometimes."
    else:
        return "I'm not sure how to respond to that, but I'm here for you!"
