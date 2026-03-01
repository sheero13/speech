#HARDCODED_VER

# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# import numpy as np

# documents = [
#     "I love machine learning and natural language processing",
#     "Information retrieval is part of natural language processing",
#     "Python is great for machine learning",
#     "Deep learning advances artificial intelligence"
# ]

# vectorizer = TfidfVectorizer()

# tfidf_matrix = vectorizer.fit_transform(documents)

# query = "machine learning in python"

# query_vector = vectorizer.transform([query])

# similarities = cosine_similarity(query_vector, tfidf_matrix)

# ranked_doc_indices = np.argsort(similarities[0])[::-1]

# print("Query:", query)
# print("\nTop matching documents:")

# for idx in ranked_doc_indices:
#     print(f"\nScore: {similarities[0][idx]:.4f}")
#     print("Document:", documents[idx])


#-----------------------------------------------------------------------------------------

#DOC_UPLOAD_VER

# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# import numpy as np
# import re

# with open("doc1.txt", "r", encoding="utf-8") as f:
#     text1 = f.read()

# with open("doc2.txt", "r", encoding="utf-8") as f:
#     text2 = f.read()

# combined_text = text1 + " " + text2
# documents = re.split(r'(?<=[.!?])\s+', combined_text)

# documents = [doc.strip() for doc in documents if doc.strip()]
# vectorizer = TfidfVectorizer(
#     stop_words='english',
#     lowercase=True,
#     ngram_range=(1,2)
# )

# tfidf_matrix = vectorizer.fit_transform(documents)

# query = input("Enter your query: ")
# query_vector = vectorizer.transform([query])
# similarities = cosine_similarity(query_vector, tfidf_matrix)

# ranked_indices = np.argsort(similarities[0])[::-1]

# print("\nTop Matching Sentences:\n")

# top_k = 5 

# for idx in ranked_indices[:top_k]:
#     print(f"Score: {similarities[0][idx]:.4f}")
#     print("Sentence:", documents[idx])
#     print()
