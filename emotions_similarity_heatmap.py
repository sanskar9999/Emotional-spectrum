import nltk
from nltk.corpus import wordnet
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# List of emotions
emotions = ['Euphoria', 'Ecstasy', 'Joy', 'Love', 'Happiness', 'Gratitude', 'Contentment', 'Hope', 'Pride', 'Amusement', 'Wonder', 'Curiosity', 'Awe', 'Nostalgia', 'Serenity', 'Calmness', 'Surprise', 'Anticipation', 'Boredom', 'Ambivalence', 'Confusion', 'Melancholy', 'Longing', 'Disappointment', 'Regret', 'Envy', 'Sadness', 'Anxiety', 'Fear', 'Frustration', 'Anger', 'Resentment', 'Rage', 'Despair', 'Hopelessness']

# Download the WordNet corpus if not already downloaded
nltk.download('wordnet')

# Create a similarity matrix
similarity_matrix = np.zeros((len(emotions), len(emotions)))

# Calculate the similarity between emotions
for i in range(len(emotions)):
    for j in range(i+1, len(emotions)):
        emotion1 = wordnet.synsets(emotions[i])[0]
        emotion2 = wordnet.synsets(emotions[j])[0]
        similarity = emotion1.wup_similarity(emotion2)
        similarity_matrix[i, j] = similarity
        similarity_matrix[j, i] = similarity

# Create a heatmap of the similarity matrix
plt.figure(figsize=(10, 8))
sns.heatmap(similarity_matrix, annot=False, cmap='coolwarm', xticklabels=emotions, yticklabels=emotions)
plt.title('Emotion Similarity Heatmap')
plt.xticks(rotation=90)
plt.yticks(rotation=0)
plt.show()
