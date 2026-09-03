"""Minimal educational TF-IDF implementation from scratch.

This file intentionally favors clarity over performance. It exposes the
intermediate quantities that high-level vectorizers usually hide.
"""

from __future__ import annotations

from collections import Counter
from math import log, sqrt
from typing import Iterable


def tokenize(text: str) -> list[str]:
    """Lowercase and split on whitespace for a deliberately simple tokenizer."""
    return text.lower().split()


def build_vocabulary(documents: Iterable[str]) -> list[str]:
    """Return a sorted vocabulary over all documents."""
    vocab = set()
    for document in documents:
        vocab.update(tokenize(document))
    return sorted(vocab)


def document_frequencies(documents: list[str], vocabulary: list[str]) -> dict[str, int]:
    """Count how many documents contain each term at least once."""
    dfs = {term: 0 for term in vocabulary}
    for document in documents:
        present_terms = set(tokenize(document))
        for term in present_terms:
            if term in dfs:
                dfs[term] += 1
    return dfs


def inverse_document_frequencies(
    documents: list[str],
    vocabulary: list[str],
    *,
    smooth: bool = True,
) -> dict[str, float]:
    """Compute IDF values.

    When smooth=True, use the same broad form used by scikit-learn:

        idf(t) = log((1 + N) / (1 + df(t))) + 1

    When smooth=False, use the classic unsmoothed form:

        idf(t) = log(N / df(t))
    """
    n_documents = len(documents)
    dfs = document_frequencies(documents, vocabulary)

    if smooth:
        return {
            term: log((1 + n_documents) / (1 + dfs[term])) + 1
            for term in vocabulary
        }

    return {
        term: log(n_documents / dfs[term])
        for term in vocabulary
        if dfs[term] > 0
    }


def term_frequency(tokens: list[str], term: str, *, normalized: bool = False) -> float:
    """Compute raw-count or length-normalized term frequency."""
    count = tokens.count(term)
    if not normalized:
        return float(count)

    if not tokens:
        return 0.0
    return count / len(tokens)


def l2_normalize(vector: list[float]) -> list[float]:
    """Return an L2-normalized vector, preserving an all-zero vector."""
    norm = sqrt(sum(value * value for value in vector))
    if norm == 0:
        return vector
    return [value / norm for value in vector]


def tfidf_transform(
    documents: list[str],
    *,
    normalized_tf: bool = False,
    smooth_idf: bool = True,
    l2_norm: bool = True,
) -> tuple[list[str], list[list[float]], dict[str, int], dict[str, float]]:
    """Convert documents into a TF-IDF matrix.

    Returns:
        vocabulary,
        matrix,
        document-frequency mapping,
        IDF mapping
    """
    vocabulary = build_vocabulary(documents)
    dfs = document_frequencies(documents, vocabulary)
    idfs = inverse_document_frequencies(
        documents,
        vocabulary,
        smooth=smooth_idf,
    )

    matrix: list[list[float]] = []

    for document in documents:
        tokens = tokenize(document)
        row = [
            term_frequency(tokens, term, normalized=normalized_tf) * idfs[term]
            for term in vocabulary
        ]

        if l2_norm:
            row = l2_normalize(row)

        matrix.append(row)

    return vocabulary, matrix, dfs, idfs


def print_matrix(vocabulary: list[str], matrix: list[list[float]]) -> None:
    """Print a compact matrix for inspection."""
    print("vocabulary:", vocabulary)
    for index, row in enumerate(matrix, start=1):
        rounded = [round(value, 4) for value in row]
        print(f"D{index}: {rounded}")


if __name__ == "__main__":
    corpus = [
        "machine learning is useful",
        "machine learning is powerful",
        "statistics is useful",
    ]

    vocabulary, matrix, dfs, idfs = tfidf_transform(corpus)

    print("Document frequencies:")
    for term in vocabulary:
        print(f"  {term:<12} -> {dfs[term]}")

    print("\nIDF values:")
    for term in vocabulary:
        print(f"  {term:<12} -> {idfs[term]:.4f}")

    print("\nTF-IDF matrix:")
    print_matrix(vocabulary, matrix)
