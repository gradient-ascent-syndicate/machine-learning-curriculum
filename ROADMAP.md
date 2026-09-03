# Learning Roadmap

This roadmap describes sensible paths through the curriculum. It is not a rigid sequence: machine learning is a dependency graph, and different goals require different branches.

## Core path

```text
Python & numerical computing
        ↓
Linear algebra + calculus + probability + statistics
        ↓
Data handling + experimentation
        ↓
ML fundamentals
        ↓
Supervised + unsupervised learning
        ↓
Neural networks & deep learning
        ↓
Choose one or more specializations
```

## Foundations

Before going deep into models, be comfortable with:

- Python syntax, functions, classes, environments, debugging, and testing;
- NumPy and vectorized numerical computation;
- pandas or equivalent tabular data manipulation;
- vectors, matrices, dot products, norms, eigenvalues/eigenvectors, and SVD intuition;
- derivatives, partial derivatives, gradients, Jacobian/Hessian intuition, and the chain rule;
- probability, random variables, expectation, variance, conditional probability, Bayes' rule, and likelihood;
- descriptive statistics, estimation, confidence intervals, hypothesis testing, and experimental design;
- optimization intuition, especially gradient-based optimization.

You do not need theorem-proof mastery before beginning ML. Learn foundations to the depth required by the next topic, then revisit them as models demand more.

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
SVM + kernel methods
   ↓
Clustering + PCA
   ↓
Model selection + calibration + interpretability
```

## Neural Networks & Deep Learning path

```text
Linear algebra + calculus + optimization
   ↓
Perceptron
   ↓
MLP + activation functions + losses
   ↓
Forward propagation
   ↓
Backpropagation
   ↓
SGD / momentum / Adam
   ↓
Initialization + normalization + regularization
   ↓
Deep architectures
   ├── CNNs ───────────────→ Computer Vision
   ├── RNN/LSTM/GRU ──────→ Sequence Modeling
   ├── Attention
   │      ↓
   │   Transformers ──────→ NLP / LLMs / Multimodal
   └── Generative Models ─→ Generative AI
```

A learner should implement a small neural network and backpropagation manually at least once before relying completely on framework abstractions.

## NLP path

```text
Foundations
   ↓
ML fundamentals
   ↓
Text preprocessing + tokenization
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
Fine-tuning + evaluation
   ↓
Retrieval / RAG
   ↓
LLM systems
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
Self-supervised vision
   ↓
Vision-language / multimodal models
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
SARSA / Q-learning
   ↓
Function approximation
   ↓
Policy gradients
   ↓
Actor-critic methods
   ↓
Deep RL
   ↓
Offline / model-based / multi-agent concepts
```

## Generative AI & LLM path

```text
NLP foundations
   +
Deep learning
   ↓
Transformers
   ↓
Language-model objectives
   ↓
Pretraining concepts
   ↓
Tokenization + data + scaling
   ↓
Instruction tuning / SFT
   ↓
Preference learning concepts
   ↓
Decoding + inference
   ↓
Prompting + in-context learning
   ↓
Retrieval + RAG
   ↓
LLM evaluation + reliability
   ↓
Production LLM systems
```

## Agentic AI path

```text
LLM competence
   +
APIs / software engineering
   +
Evaluation fundamentals
   ↓
Function/tool calling
   ↓
State + memory
   ↓
Workflow orchestration
   ↓
Planning / decomposition / verification
   ↓
Single-agent systems
   ↓
Human-in-the-loop patterns
   ↓
Multi-agent concepts
   ↓
Agent evaluation
   ↓
Durable production agents
```

Agents should be learned as systems, not as prompt templates. Evaluation, state management, permissions, tool reliability, failure recovery, latency, and cost are part of the topic.

## Specialized ML paths

After core ML, learners may branch into:

```text
Time Series & Forecasting
Recommender Systems
Graph Machine Learning
Causal Machine Learning
Probabilistic Machine Learning
Survival Analysis
Learning to Rank
Active / Online / Multi-task Learning
```

Each specialization has its own prerequisites. For example, causal ML benefits from stronger statistics, while graph ML often benefits from deep-learning competence.

## ML Engineering & MLOps path

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
Scalable training and inference
```

## AI Evaluation path

```text
Statistics + experimental design
   ↓
Task definition
   ↓
Metrics + rubrics
   ↓
Human and automatic evaluation
   ↓
Slice analysis + confidence
   ↓
LLM / retrieval / RAG evaluation
   ↓
Agent evaluation
   ↓
Robustness + reliability evaluation
   ↓
Continuous production evaluation
```

Evaluation should be learned early and revisited at every layer. A system that cannot be evaluated cannot be improved systematically.

## AI Systems & Infrastructure path

```text
ML engineering
   +
Deep-learning systems knowledge
   ↓
GPU/accelerator fundamentals
   ↓
Distributed training concepts
   ↓
Inference optimization
   ↓
Serving architectures
   ↓
Retrieval infrastructure
   ↓
Observability
   ↓
AI platform engineering
   ↓
Reliability + cost + capacity engineering
```

## A possible full-stack AI/ML path

For someone who wants unusually broad competence across the field:

```text
Foundations
→ Data & experimentation
→ ML fundamentals
→ Classical supervised/unsupervised ML
→ Neural networks & deep learning
→ NLP + CV fundamentals
→ Transformers
→ Generative AI & LLMs
→ Retrieval & RAG
→ Evaluation
→ Agents
→ ML Engineering & MLOps
→ AI Systems & Infrastructure
→ Pick deeper specializations and research topics
```

This is a multi-year map, not a checklist to rush through.

## Completion principle

Do not mark a topic complete because you watched a video or copied a notebook. A topic is complete when you can explain it, derive or reason about its key mechanics, implement or use it correctly, design an experiment around it, interpret the result, identify failure modes, and know when a different method would be preferable.
