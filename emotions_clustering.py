import nltk
from nltk.corpus import wordnet
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# List of emotions
emotions = ['Euphoria', 'Ecstasy', 'Joy', 'Love', 'Happiness', 'Gratitude', 'Contentment', 'Hope', 'Pride', 'Amusement', 'Wonder', 'Curiosity', 'Awe', 'Nostalgia', 'Serenity', 'Calmness', 'Surprise', 'Anticipation', 'Boredom', 'Ambivalence', 'Confusion', 'Melancholy', 'Longing', 'Disappointment', 'Regret', 'Envy', 'Sadness', 'Anxiety', 'Fear', 'Frustration', 'Anger', 'Resentment', 'Rage', 'Despair', 'Hopelessness']

# Download the WordNet corpus if not already downloaded
nltk.download('wordnet')

# Calculate the semantic similarity between emotions
similarity_matrix = []
for i in range(len(emotions)):
    row = []
    for j in range(len(emotions)):
        emotion1 = wordnet.synsets(emotions[i])[0]
        emotion2 = wordnet.synsets(emotions[j])[0]
        similarity = emotion1.wup_similarity(emotion2)
        row.append(similarity)
    similarity_matrix.append(row)

# Perform K-Means clustering
kmeans = KMeans(n_clusters=5)
kmeans.fit(similarity_matrix)

# Visualize the clustering results using a dendrogram
linked = linkage(similarity_matrix, 'ward')
plt.figure(figsize=(10, 8))
dendrogram(linked, labels=emotions, orientation='left')
plt.title('Emotion Clustering Dendrogram')
plt.show()
