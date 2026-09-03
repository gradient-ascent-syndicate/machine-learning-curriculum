# TF-IDF — Term Frequency–Inverse Document Frequency

> **Goal:** learn why raw word counts are often a poor representation of importance, derive TF-IDF, implement it from scratch, use a standard library implementation correctly, and understand where the method succeeds and fails.

## Why this topic matters

A Bag-of-Words representation tells us **which words occur and how often**, but frequency alone is not the same as importance.

Consider two words in a collection of documents:

- `the` appears in almost every document;
- `photosynthesis` appears in only a few biology documents.

Raw counts may make `the` look important simply because it occurs often. TF-IDF corrects this by combining two ideas:

1. a term should receive more weight when it appears often in a document;
2. a term should receive less weight when it appears in many documents across the corpus.

That simple idea became one of the foundational weighting schemes in information retrieval and classical NLP.

---

## Prerequisites

Before starting, you should be comfortable with:

- basic Python;
- dictionaries, lists, and loops;
- tokenization and simple text preprocessing;
- Bag of Words / count vectors;
- vectors and dot products at an intuitive level;
- logarithms.

Helpful internal prerequisites:

- `text preprocessing` — planned unit
- `Bag of Words` — planned unit

---

## Learning objectives

By the end of this unit, you should be able to:

- explain **term frequency**, **document frequency**, **inverse document frequency**, and **TF-IDF** in plain language;
- derive common TF and IDF formulations;
- explain why corpus-wide common terms are down-weighted;
- calculate TF-IDF by hand for a tiny corpus;
- implement TF-IDF without using a high-level vectorizer;
- use `sklearn.feature_extraction.text.TfidfVectorizer` correctly;
- explain smoothing, normalization, sublinear TF, vocabulary, and n-gram choices;
- compare raw counts against TF-IDF experimentally;
- describe important limitations of TF-IDF.

---

# 🟢 Level 1 — LEARN

## 1. Start with Bag of Words

Suppose our corpus contains three documents:

```text
D1: cats chase mice
D2: cats eat fish
D3: dogs chase cats
```

A count representation might look like:

| document | cats | chase | mice | eat | fish | dogs |
|---|---:|---:|---:|---:|---:|---:|
| D1 | 1 | 1 | 1 | 0 | 0 | 0 |
| D2 | 1 | 0 | 0 | 1 | 1 | 0 |
| D3 | 1 | 1 | 0 | 0 | 0 | 1 |

The representation is useful, but notice that `cats` occurs in **every document**. It does not help much to distinguish one document from another.

That is the central motivation for IDF.

---

## 2. Term Frequency (TF)

Term Frequency asks:

> **How important is this term inside this document?**

The simplest form is the raw count:

\[
TF(t,d) = f_{t,d}
\]

where \(f_{t,d}\) is the number of times term \(t\) appears in document \(d\).

A normalized version is:

\[
TF(t,d) = \frac{f_{t,d}}{\sum_{t'} f_{t',d}}
\]

This prevents longer documents from receiving larger values simply because they contain more words.

Another common choice is **sublinear term frequency**:

\[
TF(t,d) = 1 + \log(f_{t,d})
\]

for \(f_{t,d} > 0\).

The intuition is that seeing a term 20 times instead of 10 times usually should not make it twice as important.

---

## 3. Document Frequency (DF)

Document Frequency asks:

> **In how many documents does this term appear?**

\[
DF(t) = |\{d : t \in d\}|
\]

If `cats` appears in all 3 documents, then:

\[
DF(\text{cats}) = 3
\]

If `mice` appears only in D1:

\[
DF(\text{mice}) = 1
\]

A low document frequency usually means the term is more useful for distinguishing documents.

---

## 4. Inverse Document Frequency (IDF)

IDF transforms document frequency into a weight that becomes **smaller for globally common terms**.

A classic formulation is:

\[
IDF(t) = \log\left(\frac{N}{DF(t)}\right)
\]

where \(N\) is the total number of documents.

For the three-document corpus:

\[
IDF(\text{cats}) = \log(3/3) = 0
\]

while:

\[
IDF(\text{mice}) = \log(3/1)
\]

So `cats`, which appears everywhere, receives almost no discriminative weight, while `mice`, which appears in one document, receives more.

### Why the logarithm?

Without the logarithm, the ratio \(N / DF(t)\) can grow very quickly. The logarithm compresses that range and makes the weighting less extreme.

---

## 5. TF-IDF

TF-IDF multiplies the local importance of a term by its global rarity:

\[
TFIDF(t,d) = TF(t,d) \times IDF(t)
\]

The resulting weight is high when a term:

- occurs meaningfully in the current document; and
- is relatively uncommon across the corpus.

It is low when a term:

- barely appears in the document; or
- appears in almost every document.

That is the entire core idea.

---

# 🟡 Level 2 — DERIVE / BUILD

## 6. A hand calculation

Use this corpus:

```text
D1: machine learning is useful
D2: machine learning is powerful
D3: statistics is useful
```

Focus on the term `useful`.

### Step 1 — document frequency

`useful` occurs in D1 and D3, so:

\[
DF(\text{useful}) = 2
\]

There are 3 documents:

\[
N = 3
\]

### Step 2 — IDF

Using the unsmoothed formulation:

\[
IDF(\text{useful}) = \log(3/2)
\]

### Step 3 — TF in D1

If we use raw counts:

\[
TF(\text{useful}, D1)=1
\]

### Step 4 — TF-IDF

\[
TFIDF(\text{useful},D1)=1 \times \log(3/2)
\]

Repeat this exercise for:

- `machine`;
- `is`;
- `powerful`.

Notice how corpus-wide common terms receive smaller IDF values.

---

## 7. Smoothed IDF

Real libraries often use smoothed variants to avoid edge cases and improve numerical behavior.

A common smoothed form is:

\[
IDF(t) = \log\left(\frac{1+N}{1+DF(t)}\right)+1
\]

Scikit-learn uses this form when `smooth_idf=True`.

The extra `+1` terms prevent division by zero in situations where a vocabulary contains a term not observed in the fitted corpus, and the final `+1` keeps terms from receiving an IDF of zero when they occur in every document.

This means **different implementations may produce different numeric TF-IDF values while expressing the same basic principle**.

Always inspect the exact formulation used by your library.

---

## 8. Vector normalization

After computing TF-IDF weights, a document vector is often normalized.

With L2 normalization:

\[
\hat{x} = \frac{x}{\|x\|_2}
\]

This makes each document vector have Euclidean norm 1.

Why do this?

Because downstream comparisons—especially cosine similarity—should usually depend on the **direction** of the vector rather than its raw magnitude.

Scikit-learn defaults to `norm="l2"`.

---

## 9. From-scratch implementation

Open [`from_scratch.py`](from_scratch.py).

The implementation deliberately separates:

1. tokenization;
2. vocabulary construction;
3. document frequency;
4. IDF;
5. term frequency;
6. TF-IDF;
7. optional L2 normalization.

Do not skip directly to the final matrix. Understanding the intermediate quantities is the point of the exercise.

### Tasks

- run the implementation on the example corpus;
- print the vocabulary;
- print document frequencies;
- print IDF values;
- inspect the unnormalized TF-IDF matrix;
- enable normalization and compare the result.

---

# 🟠 Level 3 — USE / EXPERIMENT

## 10. Scikit-learn implementation

Open [`sklearn_example.py`](sklearn_example.py).

The most important parameters to understand are:

| parameter | what it controls |
|---|---|
| `lowercase` | lowercases text before tokenization |
| `stop_words` | optionally removes predefined stop words |
| `ngram_range` | includes unigrams, bigrams, etc. |
| `min_df` | ignores terms appearing in too few documents |
| `max_df` | ignores terms appearing in too many documents |
| `max_features` | caps vocabulary size |
| `binary` | uses occurrence instead of count before IDF |
| `sublinear_tf` | uses `1 + log(tf)` instead of raw frequency |
| `smooth_idf` | enables smoothed IDF |
| `norm` | controls vector normalization |

A high-level API is easy to call. The skill is understanding what choices it is making for you.

---

## 11. Experiments

Work through [`experiments.md`](experiments.md).

The experiments are designed to answer questions such as:

- How does TF-IDF differ from raw count vectors?
- How does adding many repeated occurrences of one word affect TF-IDF?
- What changes when a rare term becomes common across the corpus?
- What does `sublinear_tf=True` change?
- How do `min_df` and `max_df` alter the vocabulary?
- What happens when bigrams are introduced?
- Why is TF-IDF corpus-dependent?

Do not treat plots or tables as decoration. Each experiment should end with a written interpretation.

---

# 🔴 Level 4 — EXTEND

Choose one or more:

1. implement multiple TF formulations and compare them;
2. implement multiple IDF formulations and explain their differences;
3. build a tiny document search engine using TF-IDF + cosine similarity;
4. compare TF-IDF classification against raw count vectors on a text dataset;
5. compare TF-IDF against static word embeddings or transformer embeddings on a retrieval/classification task;
6. study BM25 and explain how it extends the same family of information-retrieval intuitions.

---

# Failure modes and trade-offs

TF-IDF is powerful because it is simple, sparse, interpretable, and cheap. It is also limited.

## 1. It does not understand meaning

`car` and `automobile` are unrelated dimensions unless preprocessing or vocabulary construction explicitly connects them.

## 2. It largely ignores word order

A unigram TF-IDF representation cannot distinguish well between phrases whose meaning depends on order.

N-grams partially help, but increase dimensionality.

## 3. It is corpus-dependent

IDF values are defined relative to the fitted corpus. Change the corpus and the same word may receive a different weight.

## 4. It produces high-dimensional sparse vectors

Large vocabularies create very wide feature matrices.

## 5. Rare does not always mean important

Typos, identifiers, random strings, or noisy tokens may receive high IDF values simply because they are rare.

## 6. Preprocessing decisions matter

Tokenization, casing, punctuation handling, stemming, lemmatization, stop-word removal, and n-gram choices can materially change the representation.

## 7. It has no contextual representation

The word `bank` gets the same feature dimension whether it refers to a financial institution or a river bank.

---

# When TF-IDF is still a strong choice

Despite modern embedding methods, TF-IDF remains an excellent baseline when:

- data is limited;
- interpretability matters;
- compute or latency budgets are small;
- exact lexical overlap is important;
- you need a strong sparse retrieval/classification baseline;
- you want to understand whether a complex model actually adds value.

A sophisticated model should usually beat a well-built simple baseline, not merely avoid being compared with one.

---

# Exercises

Complete [`exercises.md`](exercises.md).

At minimum, do the conceptual questions, one hand calculation, the from-scratch implementation tasks, and two experiments.

---

# Completion checklist

You can consider this unit complete when you can:

- [ ] explain TF, DF, IDF, and TF-IDF without reading notes;
- [ ] derive a standard TF-IDF equation;
- [ ] calculate TF-IDF manually for a tiny corpus;
- [ ] explain why logarithms and smoothing are used;
- [ ] implement TF-IDF from scratch;
- [ ] explain the difference between your implementation and scikit-learn's defaults;
- [ ] interpret the effect of L2 normalization;
- [ ] use `TfidfVectorizer` with deliberate parameter choices;
- [ ] explain at least four limitations of TF-IDF;
- [ ] name at least three situations where TF-IDF is still a strong baseline.

---

# References

Prefer primary/canonical material when expanding this unit. Useful references include:

- Gerard Salton and colleagues' foundational work on term weighting and vector-space information retrieval;
- Christopher D. Manning, Prabhakar Raghavan, and Hinrich Schütze, *Introduction to Information Retrieval*;
- scikit-learn documentation for `TfidfVectorizer` and `TfidfTransformer`.

When adding a reference, state what part of the unit it supports rather than creating an undifferentiated link dump.
