# TF-IDF Experiments

These experiments are designed to make TF-IDF behavior visible. For each one, write down your hypothesis **before** running it, then explain the result afterward.

## Experiment 1 — Raw counts vs TF-IDF

Create a corpus where one common word appears in every document and one topic-specific word appears in only one or two documents.

Compare:

- `CountVectorizer`
- `TfidfVectorizer`

Questions:

1. Which words dominate the raw count representation?
2. Which words receive the largest TF-IDF weights?
3. Which representation better separates the documents, and why?

---

## Experiment 2 — Repetition and sublinear TF

Start with:

```text
D1: python code
D2: python python python python python code
```

Compare TF-IDF with:

- `sublinear_tf=False`
- `sublinear_tf=True`

Questions:

1. How much does repeating `python` change its weight?
2. Why might logarithmic TF be more sensible for long documents?

---

## Experiment 3 — Make a rare term common

Begin with a term that appears in only one document. Then add that term to more and more documents and recompute IDF.

Record:

| number of documents containing term | IDF |
|---:|---:|
| 1 | |
| 2 | |
| 3 | |
| ... | |

Explain the curve.

---

## Experiment 4 — Smoothing

Compare `smooth_idf=True` and `smooth_idf=False`.

Questions:

1. Which terms change most?
2. What happens to a term that occurs in every document?
3. Why might a library prefer a smoothed formulation?

---

## Experiment 5 — L2 normalization

Compute TF-IDF with:

- `norm=None`
- `norm="l2"`

Use documents with very different lengths.

Questions:

1. How does document length affect unnormalized vectors?
2. What property does L2 normalization impose?
3. Why is this useful for cosine similarity?

---

## Experiment 6 — Vocabulary filtering

Use a larger corpus and vary:

- `min_df`
- `max_df`
- `max_features`

Track vocabulary size and inspect which terms disappear.

Explain the difference between:

- removing very rare terms;
- removing extremely common terms;
- simply keeping the top-N features.

---

## Experiment 7 — Unigrams vs bigrams

Compare:

```python
ngram_range=(1, 1)
```

against:

```python
ngram_range=(1, 2)
```

Use sentences containing phrases such as:

```text
machine learning
not good
new york
```

Questions:

1. What information can bigrams preserve that unigrams lose?
2. What happens to vocabulary size?
3. What new sparsity/computation trade-off appears?

---

## Experiment 8 — Corpus dependence

Fit one vectorizer on a technology corpus and another on a medical corpus. Include the same word in both corpora.

Compare its IDF values.

Explain why there is no universal, context-free TF-IDF weight for a word.

---

## Experiment 9 — Tiny search engine

1. Fit TF-IDF on 10–50 short documents.
2. Transform a user query with the fitted vectorizer.
3. Rank documents using cosine similarity.
4. Inspect the top results.

Try queries based on:

- exact lexical overlap;
- synonyms that never occur in the same lexical form;
- ambiguous words.

Use the failures to explain TF-IDF's lexical nature.

---

## Experiment 10 — Classification baseline

Choose a small labeled text dataset.

Compare a simple classifier using:

1. raw count vectors;
2. TF-IDF vectors.

Keep the classifier and data split constant.

Report at least:

- accuracy or F1 as appropriate;
- vocabulary size;
- training time;
- a short interpretation.

The goal is not to prove that TF-IDF always wins. The goal is to understand when weighting changes the downstream task.
