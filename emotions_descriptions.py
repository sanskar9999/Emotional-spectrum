import random

emotions = [
    "Euphoria", "Ecstasy", "Joy", "Love", "Happiness", "Gratitude", "Contentment", "Hope", "Pride", "Amusement",
    "Wonder", "Curiosity", "Awe", "Nostalgia", "Serenity", "Calmness", "Surprise", "Anticipation", "Boredom",
    "Ambivalence", "Confusion", "Melancholy", "Longing", "Disappointment", "Regret", "Envy", "Sadness", "Anxiety",
    "Fear", "Frustration", "Anger", "Resentment", "Rage", "Despair", "Hopelessness"
]

def get_random_emotion():
    return random.choice(emotions)

def get_emotion_description(emotion):
    descriptions = {
        "Euphoria": "An intense feeling of happiness and excitement.",
        "Ecstasy": "A state of overwhelming joy and pleasure.",
        "Joy": "A feeling of great happiness and delight.",
        "Love": "A strong affection and deep attachment towards someone or something.",
        "Happiness": "A state of contentment and positive well-being.",
        "Gratitude": "A feeling of appreciation and thankfulness.",
        "Contentment": "A state of satisfaction and peace.",
        "Hope": "A feeling of expectation and desire for a positive outcome.",
        "Pride": "A sense of satisfaction derived from one's own achievements or qualities.",
        "Amusement": "A feeling of enjoyment and entertainment.",
        "Wonder": "A sense of amazement and admiration.",
        "Curiosity": "A strong desire to learn or know something.",
        "Awe": "A feeling of reverential respect mixed with fear or wonder.",
        "Nostalgia": "A sentimental longing or affection for the past.",
        "Serenity": "A state of calmness, peace, and tranquility.",
        "Calmness": "A state of being free from agitation or excitement.",
        "Surprise": "A feeling of unexpected astonishment or amazement.",
        "Anticipation": "A feeling of excitement about something that is going to happen.",
        "Boredom": "A state of weariness and restlessness caused by lack of interest.",
        "Ambivalence": "The coexistence of opposing attitudes or feelings.",
        "Confusion": "A state of being bewildered or unclear in one's mind.",
        "Melancholy": "A feeling of pensive sadness, typically with no obvious cause.",
        "Longing": "A strong, persistent desire or craving for something.",
        "Disappointment": "A feeling of dissatisfaction that results when expectations are not met.",
        "Regret": "A feeling of sadness, repentance, or disappointment over something that has happened.",
        "Envy": "A feeling of discontented or resentful longing aroused by someone else's possessions or qualities.",
        "Sadness": "A feeling of unhappiness or sorrow.",
        "Anxiety": "A feeling of worry, nervousness, or unease about something with an uncertain outcome.",
        "Fear": "An unpleasant emotion caused by the threat of danger, pain, or harm.",
        "Frustration": "A feeling of annoyance or anger caused by the inability to change or achieve something.",
        "Anger": "A strong feeling of annoyance, displeasure, or hostility.",
        "Resentment": "A feeling of indignant displeasure or persistent ill will at something regarded as a wrong.",
        "Rage": "Violent, uncontrollable anger.",
        "Despair": "A state of complete loss of hope.",
        "Hopelessness": "A feeling of despair and lack of hope."
    }
    return descriptions.get(emotion, "No description available.")

def explore_emotions():
    print("Welcome to the Emotion Explorer!")
    while True:
        print("\nOptions:")
        print("1. Explore a random emotion")
        print("2. Quit")
        choice = input("Enter your choice (1-2): ")
        if choice == "1":
          emotion = get_random_emotion()
          description = get_emotion_description(emotion)
          print(f"\nEmotion: {emotion}")
          print(f"Description: {description}")
        elif choice == "2":
          print("Thank you for exploring emotions. Goodbye!")
          break
        else:
          print("Invalid choice. Please try again.")

explore_emotions()
