# Emotional-spectrum
Analysis of the human emotional spectrum

# Emotion Explorer

## Overview
The Emotion Explorer is a project designed to explore and analyze a list of emotions using various techniques including word clouds, descriptive analysis, clustering, and visualization. This project aims to provide insights into the rich landscape of human emotions, their descriptions, occurrences, and relationships.

The project consists of several Python scripts, each serving a specific purpose:

1. `emotions_wordcloud.py`: Generates a word cloud visualizing the list of emotions.
2. `emotions_descriptions.py`: Provides descriptions for each emotion and allows exploration of emotions interactively.
3. `emotions_clustering.py`: Performs K-Means clustering on the emotions and visualizes the results using a dendrogram.
4. `emotions_occurrence.py`: Counts the occurrence of each emotion in WordNet and creates a bar chart.
5. `emotions_similarity_heatmap.py`: Calculates the semantic similarity between emotions and creates a heatmap to visualize the similarity matrix.

To run any of these scripts, simply execute them using Python from the command line or your preferred IDE.

## Description <a name="description"></a>
The project begins with the generation of a word cloud representing the list of emotions. Each emotion is visualized with a font size proportional to its importance or frequency in the list.

## Exploration <a name="exploration"></a>
The `emotions_descriptions.py` script allows users to explore emotions interactively. Users can choose to explore a random emotion and receive a description of that emotion. This interactive exploration provides insights into the diverse range of human emotions and their nuanced meanings.

## Analysis <a name="analysis"></a>
The project further delves into the analysis of emotions through clustering and visualization. The `emotions_clustering.py` script performs K-Means clustering on the semantic similarity matrix of emotions and visualizes the clustering results using a dendrogram. Additionally, the `emotions_similarity_heatmap.py` script creates a heatmap to visualize the semantic similarity between emotions, providing a comprehensive understanding of their relationships.
