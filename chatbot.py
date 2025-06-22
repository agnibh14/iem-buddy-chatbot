import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load FAQs from file (make sure path is correct)
with open('data/faqs.json', 'r', encoding='utf-8') as f:
    faqs = json.load(f)

questions = [item['question'] for item in faqs]
answers = [item['answer'] for item in faqs]

# Create and fit the TF-IDF vectorizer on questions
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

def get_answer(query):
    query_vec = vectorizer.transform([query])
    similarity = cosine_similarity(query_vec, X).flatten()
    idx = np.argmax(similarity)
    if similarity[idx] < 0.3:
        return "Sorry, I don't understand your question."
    else:
        return answers[idx]
