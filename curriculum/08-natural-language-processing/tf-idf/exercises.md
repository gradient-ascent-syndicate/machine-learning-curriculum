# TF-IDF Exercises

## Part A — Conceptual

1. Why can raw word frequency be a poor proxy for importance?
2. What is the difference between term frequency and document frequency?
3. Why does IDF decrease as document frequency increases?
4. Why is a logarithm commonly used in IDF?
5. Why might a term that appears in every document receive very little discriminative weight?
6. Why is TF-IDF corpus-dependent?
7. Why can rare misspellings accidentally receive large weights?
8. What information does unigram TF-IDF discard?
9. What does L2 normalization change about a document vector?
10. Why is TF-IDF still useful even when transformer embeddings exist?

---

## Part B — Hand calculation

Use this corpus:

```text
D1: data science science
D2: data engineering
D3: machine learning
```

Using raw-count TF and the unsmoothed formula:

\[
IDF(t)=\log(N/DF(t))
\]

calculate:

1. `DF(data)`
2. `DF(science)`
3. `DF(machine)`
4. `IDF(data)`
5. `IDF(science)`
6. `IDF(machine)`
7. `TFIDF(science, D1)`
8. `TFIDF(data, D1)`
9. Explain which term is most discriminative and why.

Then redo the calculation using length-normalized TF.

---

## Part C — Build

Starting from `from_scratch.py`:

1. add sublinear TF;
2. add an option for L1 normalization;
3. support a user-supplied vocabulary;
4. handle empty documents gracefully;
5. compare your output numerically with scikit-learn for the same configuration.

Document every place where the outputs differ and explain why.

---

## Part D — Debugging

A learner computes document frequency by counting every occurrence of a term across the corpus rather than counting how many **documents** contain the term.

1. Explain the bug.
2. Construct a corpus where this mistake creates a dramatic error.
3. Show the incorrect and correct IDF values.

---

## Part E — Design decisions

For each scenario, choose reasonable TF-IDF settings and justify them.

### Scenario 1 — Short support tickets

Most documents are 5–30 words long and contain product names and error codes.

Discuss:

- stop-word removal;
- `min_df`;
- rare tokens;
- n-grams;
- normalization.

### Scenario 2 — Long news articles

Documents vary greatly in length.

Discuss:

- sublinear TF;
- normalization;
- common-word filtering;
- bigrams.

### Scenario 3 — Search over technical documentation

Exact phrases and identifiers matter.

Discuss:

- lexical overlap;
- n-grams;
- whether aggressive stemming is desirable;
- why TF-IDF might remain competitive with embeddings for some queries.

---

## Part F — Reflection

Write 150–300 words answering:

> If TF-IDF does not understand semantics, why has it remained such a useful baseline for text problems?

Your answer should mention at least three of:

- sparsity;
- interpretability;
- compute cost;
- lexical matching;
- small-data behavior;
- feature inspection;
- baseline discipline.

---

## Optional challenge

Build a tiny search engine using TF-IDF and cosine similarity.

Requirements:

- at least 20 documents;
- at least 5 test queries;
- ranked results;
- one example where lexical retrieval works very well;
- one example where it fails because of synonymy or context;
- a short discussion of what BM25 or dense embeddings might improve.
