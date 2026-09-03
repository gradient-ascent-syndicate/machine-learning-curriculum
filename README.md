# Machine Learning Curriculum

> **You do not learn machine learning by reading this repository. You learn it by helping build it.**

An open, contributor-built, executable curriculum for learning machine learning from first principles to advanced AI systems.

This repository is maintained by the **Gradient Ascent Syndicate**. It is designed to work in two directions:

- **Learner → Contributor:** pick a topic, follow its learning contract, study it, implement it, experiment with it, and submit your work.
- **Contributor → Future Learner:** accepted contributions become reusable learning material for the next person.

The goal is not to collect links or notebooks. The goal is to build a coherent, reviewable, hands-on machine-learning textbook where each chapter is executable.

## How it works

Every learning unit should answer seven questions:

1. What should I already know?
2. What will I learn?
3. What should I read or understand?
4. What should I derive or reason through?
5. What should I implement?
6. What experiments should I run?
7. What proves that I have actually understood the topic?

We standardize each topic around six activities:

- **LEARN** — explain the intuition and core concepts.
- **DERIVE** — work through the mathematics where relevant.
- **BUILD** — implement the idea from scratch when practical.
- **USE** — apply a standard library or production implementation.
- **EXPERIMENT** — vary assumptions, hyperparameters, data, and edge cases.
- **REFLECT** — document failure modes, trade-offs, and when not to use it.

## Curriculum map

The curriculum is organized as a knowledge graph rather than a flat resource list.

```text
00 Foundations
   ├── Programming for ML
   ├── Linear Algebra
   ├── Calculus & Optimization
   ├── Probability
   └── Statistics

01 Data & Experimentation
   ├── Data Cleaning
   ├── EDA
   ├── Feature Engineering
   ├── Sampling
   ├── Leakage
   └── Experimental Design

02 ML Fundamentals
   ├── Train / Validation / Test
   ├── Bias vs Variance
   ├── Regularization
   ├── Cross Validation
   └── Evaluation Metrics

03 Supervised Learning
   ├── Regression
   └── Classification

04 Unsupervised Learning
   ├── Clustering
   ├── Dimensionality Reduction
   └── Anomaly Detection

05 Semi-Supervised & Self-Supervised Learning

06 Neural Networks & Deep Learning

07 Computer Vision

08 Natural Language Processing

09 Reinforcement Learning

10 ML Engineering & MLOps

11 Advanced AI Systems
   ├── Recommender Systems
   ├── Graph ML
   ├── Time Series
   ├── Causal ML
   ├── Generative Models
   ├── Retrieval & RAG
   ├── Agents
   └── AI Evaluation
```

See [`ROADMAP.md`](ROADMAP.md) for the learning paths and [`curriculum/README.md`](curriculum/README.md) for the detailed topic tree.

## Start here

### If you are learning

1. Read [`ROADMAP.md`](ROADMAP.md).
2. Pick the next topic whose prerequisites you already satisfy.
3. Open that topic's learning unit.
4. Complete its required activities.
5. Use the exercises and completion checklist to test yourself.

### If you are contributing

1. Read [`CONTRIBUTING.md`](CONTRIBUTING.md).
2. Pick or open a **Learning Unit** issue.
3. Create a branch for the topic.
4. Follow the learning-unit template in [`templates/learning-unit/`](templates/learning-unit/).
5. Submit a pull request.
6. Address peer review.
7. Once merged, your contribution becomes part of the curriculum.

## Repository structure

```text
machine-learning-curriculum/
├── README.md
├── ROADMAP.md
├── CONTRIBUTING.md
├── curriculum/
│   ├── 00-foundations/
│   ├── 01-data-and-experimentation/
│   ├── 02-ml-fundamentals/
│   ├── 03-supervised-learning/
│   ├── 04-unsupervised-learning/
│   ├── 05-semi-and-self-supervised/
│   ├── 06-deep-learning/
│   ├── 07-computer-vision/
│   ├── 08-natural-language-processing/
│   ├── 09-reinforcement-learning/
│   ├── 10-ml-engineering/
│   └── 11-advanced-ai-systems/
└── templates/
    └── learning-unit/
```

## Contribution philosophy

A contribution should teach, not merely demonstrate that code runs.

A strong learning unit usually contains:

- intuitive explanation;
- mathematical formulation where relevant;
- from-scratch implementation where educationally useful;
- standard-library implementation;
- experiments and visualizations;
- exercises;
- failure cases and trade-offs;
- references to high-quality primary or canonical material.

A notebook dump, copied tutorial, or API-only demo is not sufficient by itself.

## Difficulty levels

Learning units may label activities using:

- 🟢 **Level 1 — Understand**
- 🟡 **Level 2 — Implement**
- 🟠 **Level 3 — Experiment**
- 🔴 **Level 4 — Extend / Research**

## License

This project is licensed under the [Apache License 2.0](LICENSE).
