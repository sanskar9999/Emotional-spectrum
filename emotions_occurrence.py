import nltk
from nltk.corpus import wordnet
import matplotlib.pyplot as plt

# List of emotions
emotions = ['Euphoria', 'Ecstasy', 'Joy', 'Love', 'Happiness', 'Gratitude', 'Contentment', 'Hope', 'Pride', 'Amusement', 'Wonder', 'Curiosity', 'Awe', 'Nostalgia', 'Serenity', 'Calmness', 'Surprise', 'Anticipation', 'Boredom', 'Ambivalence', 'Confusion', 'Melancholy', 'Longing', 'Disappointment', 'Regret', 'Envy', 'Sadness', 'Anxiety', 'Fear', 'Frustration', 'Anger', 'Resentment', 'Rage', 'Despair', 'Hopelessness']

# Download the WordNet corpus if not already downloaded
nltk.download('wordnet')

# Count the occurrence of each emotion in WordNet
emotion_frequency = {emotion: 0 for emotion in emotions}
for emotion in emotions:
    synsets = wordnet.synsets(emotion)
    emotion_frequency[emotion] = len(synsets)

# Create a bar chart
plt.figure(figsize=(12, 6))
plt.bar(emotion_frequency.keys(), emotion_frequency.values(), color='skyblue')
plt.xlabel('Emotion')
plt.ylabel('Frequency')
plt.title('Emotion Occurrence in WordNet')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
