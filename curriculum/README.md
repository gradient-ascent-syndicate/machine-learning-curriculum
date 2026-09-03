# Curriculum

This directory contains the topic graph for the Machine Learning Curriculum. The structure is intentionally broad: it should support a learner starting from Python and statistics, but also provide clear paths into deep learning, computer vision, NLP, LLMs, agents, evaluation, and production AI systems.

## 00 — Foundations

### Programming for ML
- Python essentials
- functions, classes, modules
- environments and dependency management
- debugging and testing
- NumPy
- pandas
- visualization
- notebooks versus scripts
- reproducibility
- basic software-engineering practices for ML

### Linear Algebra
- scalars, vectors, matrices, tensors
- matrix multiplication
- linear systems
- rank and linear independence
- norms and distances
- projections
- eigenvalues/eigenvectors
- SVD
- positive-semidefinite matrices
- matrix calculus intuition

### Calculus & Optimization
- derivatives
- partial derivatives
- gradients
- Jacobians and Hessians
- chain rule
- Taylor approximation
- convexity intuition
- constrained optimization intuition
- gradient descent and ascent
- stochastic optimization
- Lagrange multipliers intuition

### Probability
- sample spaces and events
- random variables
- discrete and continuous distributions
- expectation and variance
- covariance and correlation
- conditional probability
- Bayes' rule
- independence
- law of large numbers
- central limit theorem
- likelihood

### Statistics
- descriptive statistics
- sampling
- estimators
- bias and variance of estimators
- confidence intervals
- hypothesis testing
- p-values and effect sizes
- bootstrapping
- correlation and covariance
- regression as statistical modeling
- experimental design

## 01 — Data & Experimentation

- data collection and schemas
- data types and measurement scales
- missing data
- outliers
- exploratory data analysis
- feature engineering
- scaling and transformations
- encoding categorical variables
- sampling and imbalance
- leakage
- train/test contamination
- experimental design
- A/B testing fundamentals
- reproducible data pipelines
- dataset documentation
- data quality and provenance

## 02 — Machine Learning Fundamentals

- what learning means
- hypothesis spaces
- inductive bias
- loss and objective functions
- empirical risk
- train / validation / test
- underfitting and overfitting
- bias–variance trade-off
- regularization
- cross-validation
- model selection
- hyperparameter tuning
- classification metrics
- regression metrics
- ranking metrics
- calibration
- uncertainty
- interpretability
- explainability
- fairness fundamentals
- distribution shift

## 03 — Supervised Learning

### Regression
- simple and multiple linear regression
- polynomial regression
- ridge regression
- lasso regression
- elastic net
- generalized linear model intuition
- tree-based regression
- robust regression
- quantile regression

### Classification
- logistic regression
- k-nearest neighbours
- Naive Bayes
- decision trees
- random forests
- support vector machines
- kernel methods
- gradient boosting
- XGBoost/LightGBM/CatBoost concepts
- calibrated classification

### Ensembles
- bagging
- boosting
- stacking
- blending

## 04 — Unsupervised Learning

### Clustering
- k-means
- hierarchical clustering
- DBSCAN
- Gaussian mixture models
- spectral clustering concepts

### Dimensionality reduction
- PCA
- matrix factorization
- manifold learning
- t-SNE
- UMAP

### Density and structure
- density estimation
- anomaly detection
- novelty detection
- latent-variable intuition

## 05 — Semi-Supervised & Self-Supervised Learning

- pseudo-labeling
- self-training
- consistency regularization
- representation learning
- contrastive learning
- metric learning
- masked objectives
- teacher-student methods
- pretext tasks
- transfer from self-supervised representations

## 06 — Neural Networks & Deep Learning

### Neural-network foundations
- perceptron
- neurons and affine transformations
- multilayer perceptrons
- computational graphs
- forward propagation
- activation functions
- output layers
- neural-network losses
- representation learning

### Training neural networks
- backpropagation
- automatic differentiation
- gradient checking
- SGD and mini-batch training
- momentum
- RMSProp
- Adam / AdamW
- learning-rate schedules
- initialization
- gradient clipping
- vanishing/exploding gradients

### Generalization and stability
- dropout
- weight decay
- early stopping
- data augmentation
- label smoothing
- batch normalization
- layer normalization
- residual connections
- calibration

### Core architectures
- deep MLPs
- CNNs
- RNNs
- LSTMs / GRUs
- sequence-to-sequence
- encoder-decoder models
- attention
- self-attention
- transformers
- mixture-of-experts fundamentals
- graph neural-network fundamentals
- state-space-model fundamentals

### Generative deep learning
- autoencoders
- VAEs
- autoregressive models
- GANs
- diffusion models
- score-based modeling concepts
- normalizing-flow intuition

### Practical deep learning
- PyTorch
- TensorFlow/Keras
- GPUs and accelerators
- mixed precision
- checkpointing
- profiling
- distributed-training concepts
- transfer learning
- fine-tuning
- PEFT fundamentals
- model export and serving

## 07 — Computer Vision

### Image foundations
- pixels, channels, color spaces
- resizing and interpolation
- filtering
- edges and gradients
- morphology
- classical image descriptors

### Deep vision
- CNNs in practice
- image classification
- transfer learning
- object detection
- semantic segmentation
- instance segmentation
- pose estimation
- metric learning for vision
- vision transformers
- self-supervised vision

### Generative and multimodal vision
- image generation concepts
- diffusion for images
- image-text representations
- vision-language models
- visual question answering
- image captioning
- multimodal retrieval

## 08 — Natural Language Processing

### Classical NLP
- text normalization
- tokenization
- stemming and lemmatization
- n-grams
- Bag of Words
- TF-IDF
- text classification
- sequence labeling
- topic modeling

### Representations
- distributional semantics
- word embeddings
- Word2Vec / GloVe concepts
- contextual embeddings
- sentence embeddings

### Neural NLP
- RNNs / LSTMs
- encoder-decoder models
- attention
- transformers
- sequence classification
- named-entity recognition
- question answering
- summarization
- machine translation

### Modern NLP
- language modeling
- transfer learning
- fine-tuning
- retrieval
- semantic search
- evaluation

## 09 — Reinforcement Learning

### Foundations
- agents, environments, states, actions, rewards
- Markov decision processes
- returns and discounting
- Bellman equations
- value and policy functions

### Tabular RL
- dynamic programming
- Monte Carlo methods
- temporal-difference learning
- SARSA
- Q-learning
- exploration strategies

### Deep RL
- function approximation
- deep Q-networks
- policy gradients
- actor-critic methods
- PPO concepts
- replay buffers
- target networks

### Advanced RL concepts
- offline RL
- model-based RL
- multi-agent RL
- imitation learning
- inverse RL concepts
- RL evaluation and reproducibility

## 10 — ML Engineering & MLOps

- reproducible experimentation
- dataset and feature pipelines
- training pipelines
- model packaging
- batch and online inference
- APIs and serving
- testing ML systems
- experiment tracking
- model registries
- feature stores
- orchestration
- monitoring
- data and concept drift
- CI/CD for ML
- governance and lineage
- scalable training and inference
- cost/performance trade-offs

## 11 — Specialized ML Domains

### Time series and forecasting
- temporal validation
- decomposition
- ARIMA-family models
- exponential smoothing
- state-space models
- probabilistic forecasting
- deep forecasting

### Recommender systems
- collaborative filtering
- content-based systems
- matrix factorization
- implicit feedback
- candidate generation
- ranking
- recommendation evaluation

### Graph machine learning
- graph representations
- node embeddings
- message passing
- GNNs
- node classification
- link prediction
- knowledge graphs

### Causal machine learning
- causal DAGs
- confounding
- potential outcomes
- treatment effects
- propensity methods
- causal forests
- causal discovery concepts

### Probabilistic machine learning
- Bayesian inference
- graphical models
- latent-variable models
- EM
- variational inference
- Monte Carlo methods
- uncertainty quantification

### Additional domains
- survival analysis
- learning to rank
- active learning
- online learning
- multi-task learning
- domain adaptation
- federated-learning fundamentals

## 12 — Generative AI & Large Language Models

### LLM foundations
- tokenization
- language-model objectives
- pretraining
- scaling laws
- training data

### Adaptation
- instruction tuning
- supervised fine-tuning
- preference learning
- RLHF concepts
- DPO concepts
- LoRA / PEFT
- distillation

### Inference
- decoding and sampling
- KV cache
- batching
- quantization
- speculative decoding concepts
- inference-time compute
- structured generation

### Prompting and context
- prompt design
- in-context learning
- few-shot learning
- reasoning-oriented prompting
- context management
- long-context behavior

### Retrieval-augmented generation
- sparse and dense retrieval
- embeddings
- vector search
- hybrid retrieval
- reranking
- chunking
- query rewriting
- grounded generation
- RAG evaluation

### LLM applications and reliability
- extraction
- classification
- summarization
- QA
- code generation
- tool calling
- synthetic data
- hallucination
- grounding
- uncertainty

## 13 — Agentic AI

- agents versus workflows
- environment/state/action/objective
- tool use and function calling
- planning and decomposition
- reactive and plan-execute patterns
- verification and reflection
- memory and persistent state
- router systems
- supervisor-worker systems
- multi-agent concepts
- human-in-the-loop patterns
- coding, research, and computer-use agents
- durable execution
- permissions
- observability
- agent evaluation
- production orchestration

## 14 — AI Evaluation, Safety & Alignment

- task definition and rubrics
- offline and online evaluation
- human evaluation
- automatic evaluation
- LLM-as-judge concepts
- statistical significance
- benchmark construction
- contamination and leakage
- factuality
- groundedness
- instruction following
- retrieval and RAG evaluation
- code-generation evaluation
- agent evaluation
- robustness and stress testing
- calibration and abstention
- privacy and access-control fundamentals
- reward modeling
- preference optimization
- alignment concepts
- golden datasets
- regression suites
- continuous evaluation

## 15 — AI Systems & Infrastructure

### Compute and training systems
- CPUs, GPUs, TPUs
- memory hierarchy
- distributed data parallelism
- model/tensor/pipeline parallelism concepts
- sharding
- mixed precision
- checkpointing
- fault tolerance

### Inference systems
- batching
- caching
- KV cache
- quantization
- compression
- routing
- autoscaling
- latency/throughput/cost optimization

### Serving and retrieval infrastructure
- online and batch inference
- synchronous/asynchronous serving
- queues
- streaming
- gateways
- embedding pipelines
- vector indexes
- ANN search

### Platform engineering and observability
- logs, metrics, traces
- quality telemetry
- prompt/response tracing
- experiment platforms
- model registries
- evaluation pipelines
- orchestration
- multi-tenant AI platforms
- reliability and release strategies

---

This tree will evolve. New topics should be added because they improve the learning graph, not simply because they are fashionable. Every advanced topic should point back to canonical prerequisites so the repository remains a coherent curriculum rather than a collection of disconnected tutorials.
