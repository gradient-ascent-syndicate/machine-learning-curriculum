"""TF-IDF with scikit-learn, with intermediate quantities exposed."""

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer


corpus = [
    "machine learning is useful",
    "machine learning is powerful",
    "statistics is useful",
]


print("=== Raw count baseline ===")
count_vectorizer = CountVectorizer()
count_matrix = count_vectorizer.fit_transform(corpus)
print("Vocabulary:", count_vectorizer.get_feature_names_out().tolist())
print(count_matrix.toarray())


print("\n=== TF-IDF ===")
tfidf_vectorizer = TfidfVectorizer(
    lowercase=True,
    smooth_idf=True,
    sublinear_tf=False,
    norm="l2",
)

tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)
feature_names = tfidf_vectorizer.get_feature_names_out()

print("Vocabulary:", feature_names.tolist())
print("IDF values:")
for term, idf in zip(feature_names, tfidf_vectorizer.idf_):
    print(f"  {term:<12} -> {idf:.4f}")

print("\nTF-IDF matrix:")
print(tfidf_matrix.toarray().round(4))


print("\n=== Try these next ===")
print("1. Set norm=None and inspect raw TF-IDF weights.")
print("2. Set sublinear_tf=True and repeat a word many times in one document.")
print("3. Set ngram_range=(1, 2) and inspect new bigram features.")
print("4. Experiment with min_df and max_df on a larger corpus.")
