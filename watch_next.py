import spacy

# Load
nlp = spacy.load('en_core_web_md')

# Read txt file
with open('movies.txt', 'r') as f:
    movie_descriptions = f.readlines()

# function to find the most similar movie
# https://betterprogramming.pub/the-beginners-guide-to-similarity-matching-using-spacy-782fc2922f7c
def similar_movie(input_description):
    input_doc = nlp(input_description)
    similarity_scores = []
    for description in movie_descriptions:
        # https://spacy.io
        doc = nlp(description)
        similarity_score = input_doc.similarity(doc)
        similarity_scores.append((description, similarity_score))
        # https://stackoverflow.com/questions/13669252/what-is-lambda-in-python-code-how-does-it-work-with-key-arguments-to-sorte
        # sorts the list of similarity scores in descending order
    similarity_scores.sort(key=lambda x: x[1], reverse=True)
    return similarity_scores[0][0]

# To answer the hulk question of which is similar
input_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
most_similar_movie = similar_movie(input_description)
print("Most similar movie:", most_similar_movie)

# User input for example
# user_input = input("Enter a movie description: ")
# most_similar_movie = similar_movie(user_input)
# print("Most similar movie:", most_similar_movie)