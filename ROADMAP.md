# Learning Roadmap

This roadmap describes sensible paths through the curriculum. It is not a rigid sequence: machine learning is a dependency graph, and different goals require different branches.

## Core path

```text
Python & numerical computing
        ↓
Linear algebra + probability + statistics
        ↓
Data handling + experimentation
        ↓
ML fundamentals
        ↓
Supervised + unsupervised learning
        ↓
Neural networks
        ↓
Choose a specialization
```

## Foundations

Before going deep into models, be comfortable with:

- Python syntax, functions, classes, environments, and debugging;
- NumPy and vectorized numerical computation;
- pandas or equivalent tabular data manipulation;
- vectors, matrices, dot products, norms, eigenvalues/eigenvectors;
- derivatives, partial derivatives, gradients, chain rule;
- probability, random variables, expectation, variance, conditional probability, Bayes' rule;
- descriptive statistics, estimation, confidence intervals, hypothesis testing;
- optimization intuition, especially gradient-based optimization.

You do not need mathematical maturity at theorem-proof level before beginning ML. Learn foundations to the depth required by the next topic, then revisit them as models demand more.

## Classical ML path

```text
Foundations
   ↓
Data & experimentation
   ↓
Train/validation/test + metrics
   ↓
Linear regression
   ↓
Logistic regression
   ↓
KNN / Naive Bayes
   ↓
Decision trees
   ↓
Random forests / boosting
   ↓
SVM
   ↓
Clustering + PCA
   ↓
Model selection, calibration, interpretability
```

## NLP path

```text
Foundations
   ↓
ML fundamentals
   ↓
Text preprocessing
   ↓
Bag of Words
   ↓
TF-IDF
   ↓
Distributional representations / embeddings
   ↓
Neural networks
   ↓
RNN / LSTM
   ↓
Attention
   ↓
Transformers
   ↓
Language models
   ↓
Retrieval / RAG
   ↓
LLM evaluation
   ↓
Agents and AI systems
```

## Computer Vision path

```text
Foundations
   ↓
Image representation and preprocessing
   ↓
Classical image features
   ↓
Neural networks
   ↓
CNNs
   ↓
Image classification
   ↓
Detection
   ↓
Segmentation
   ↓
Vision Transformers
   ↓
Multimodal models
```

## Reinforcement Learning path

```text
Probability + statistics
   ↓
Optimization
   ↓
ML fundamentals
   ↓
Markov decision processes
   ↓
Bellman equations
   ↓
Dynamic programming
   ↓
Monte Carlo methods
   ↓
Temporal-difference learning
   ↓
Q-learning
   ↓
Policy gradients
   ↓
Actor-critic methods
   ↓
Deep RL
```

## ML Engineering path

```text
Classical ML competence
   ↓
Reproducible experiments
   ↓
Data/version management
   ↓
Training pipelines
   ↓
Packaging and serving
   ↓
Testing ML systems
   ↓
Monitoring and drift
   ↓
CI/CD for ML
   ↓
Feature stores / model registries / orchestration
   ↓
Scalable inference and evaluation
```

## Completion principle

Do not mark a topic complete because you watched a video or copied a notebook. A topic is complete when you can explain it, implement or use it correctly, design an experiment around it, interpret the result, and identify where the method breaks down.
