import matplotlib.pyplot as plt
from wordcloud import WordCloud

# List of emotions
emotions = ['Euphoria', 'Ecstasy', 'Joy', 'Love', 'Happiness', 'Gratitude', 'Contentment', 'Hope', 'Pride', 'Amusement', 'Wonder', 'Curiosity', 'Awe', 'Nostalgia', 'Serenity', 'Calmness', 'Surprise', 'Anticipation', 'Boredom', 'Ambivalence', 'Confusion', 'Melancholy', 'Longing', 'Disappointment', 'Regret', 'Envy', 'Sadness', 'Anxiety', 'Fear', 'Frustration', 'Anger', 'Resentment', 'Rage', 'Despair', 'Hopelessness']

# Create a string of emotions
emotion_string = ' '.join(emotions)

# Create a word cloud
wordcloud = WordCloud(width = 800, height = 800, 
                      random_state=21, 
                      max_font_size = 110).generate(emotion_string)

plt.figure(figsize=(10, 10))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
