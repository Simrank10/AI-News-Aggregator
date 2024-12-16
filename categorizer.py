from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

CATEGORIES = ["technology", "sports", "business", "entertainment", "politics"]


def categories_news(articles):
    categorized_news = {category: [] for category in CATEGORIES}
    corpus = CATEGORIES + [articles["title"] for article in articles]

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(corpus)

    category_vectors = tfidf_matrix[:len(CATEGORIES)]
    article_vectors = tfidf_matrix[len(CATEGORIES):]

    for i, article_vector in enumerate(article_vectors):
        similarities = cosine_similarity(article_vector, category_vectors)
        best_category = CATEGORIES[similarities.argmax()]
        categorized_news[best_category].append(articles[i])

    return categorized_news
