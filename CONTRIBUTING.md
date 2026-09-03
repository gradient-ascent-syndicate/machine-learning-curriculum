# Contributing

Thank you for helping build the Machine Learning Curriculum.

This project is designed so that contributing is itself a learning exercise. The objective is not to maximize the number of files in the repository; it is to create material that helps another learner understand, implement, test, and reason about a topic.

## Contribution workflow

1. Pick an existing **Learning Unit** issue or open a new one.
2. Confirm the topic fits the curriculum and that obvious prerequisites are listed.
3. Create a branch using a descriptive name, for example:
   - `anirudh/tfidf`
   - `abhiram/linear-regression`
   - `feature/pca-learning-unit`
4. Copy the structure from `templates/learning-unit/` into the correct curriculum folder.
5. Complete the required learning artifacts.
6. Run your code and verify notebooks/scripts are reproducible.
7. Open a pull request into `main`.
8. Address review comments.
9. Merge only after approval.

## What a learning unit should contain

At minimum, a complete learning unit should cover:

### 1. Prerequisites

List what the learner should already understand. Link to internal curriculum units where possible.

### 2. Learning objectives

Use concrete outcomes. Prefer statements such as:

- explain why logistic regression is a classifier;
- derive binary cross-entropy from the likelihood;
- implement gradient descent using NumPy;
- diagnose poor threshold selection.

Avoid vague objectives such as "understand logistic regression."

### 3. Intuition

Explain the idea in plain language before introducing notation. Use examples, diagrams, or small synthetic datasets where useful.

### 4. Mathematics

Include the mathematical formulation when the topic depends on it. Derivations should explain why each step matters, not merely display equations.

### 5. From-scratch implementation

When educationally meaningful, implement the core idea without relying on the high-level implementation from a library.

Examples:

- TF-IDF with Python/NumPy before `TfidfVectorizer`;
- linear regression using the normal equation or gradient descent before `sklearn`;
- k-means before `sklearn.cluster.KMeans`.

Do not reimplement complex production systems purely for ritual. The purpose is understanding.

### 6. Library implementation

Show how the concept is used with a standard ecosystem such as scikit-learn, PyTorch, TensorFlow, Hugging Face, OpenCV, or another appropriate tool.

### 7. Experiments

A learning unit should ask meaningful questions of the method. Examples:

- What happens as tree depth increases?
- How does regularization affect coefficients?
- When does accuracy become misleading?
- How sensitive is k-means to initialization?
- How does corpus composition change TF-IDF weights?

### 8. Exercises

Include questions or implementation tasks that require the learner to produce an answer rather than copy one.

### 9. Failure modes and trade-offs

Document assumptions, weaknesses, computational trade-offs, and cases where another method is preferable.

### 10. References

Prefer canonical textbooks, original papers, official documentation, and high-quality educational sources. Do not copy copyrighted material into the repository.

## Expected file structure

A typical topic can look like:

```text
topic-name/
├── README.md
├── theory.md
├── intuition.md
├── from_scratch.py
├── library_implementation.py
├── experiments.ipynb
├── exercises.md
├── references.md
├── topic.yml
├── images/
└── tests/
```

Not every topic needs every file. Keep the structure proportional to the concept.

## Quality bar

A PR should be understandable to a motivated learner who has completed the listed prerequisites.

Before submitting, ask:

- Can another person run this code?
- Are important claims explained or referenced?
- Is the notation defined?
- Are outputs interpreted rather than merely displayed?
- Are edge cases discussed?
- Does the contribution teach something that was not obvious from calling a library API?

## Code style

- Use readable Python and meaningful names.
- Keep notebooks focused; move reusable code into `.py` files when appropriate.
- Do not commit secrets, API keys, virtual environments, model checkpoints, or unnecessarily large datasets.
- Prefer small public datasets or provide download instructions instead of committing large data files.
- Set random seeds where reproducibility matters.
- State package/version requirements when behavior is version-sensitive.

## Pull requests

Keep PRs scoped to one coherent learning unit or infrastructure change.

A good PR description should state:

- what was added;
- why it belongs in the curriculum;
- prerequisites;
- how the contribution was validated;
- what reviewers should pay particular attention to.

## Review philosophy

Review both **technical correctness** and **teaching quality**.

Reviewers should ask whether the contributor truly explains the concept, whether experiments support the stated conclusions, and whether a future learner could use the material without hidden context.

## Attribution

Contribute using your own GitHub account. Do not pass files to another member to commit on your behalf. Individual commits, pull requests, discussions, and reviews are part of the collaborative record of this project.
