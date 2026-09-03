# 06 — Neural Networks & Deep Learning

This track is the canonical home for the neural-network concepts that power modern computer vision, NLP, generative AI, multimodal systems, and deep reinforcement learning.

The goal is not merely to train models with PyTorch or TensorFlow. A learner should understand what a neural network computes, why it can learn, how gradients move through it, why training fails, and how modern architectures evolved from these foundations.

## Prerequisites

Before beginning this track, be comfortable with:

- vectors, matrices, matrix multiplication, dot products, norms, and basic eigendecomposition;
- derivatives, partial derivatives, gradients, the chain rule, and basic multivariable calculus;
- probability distributions, expectation, variance, likelihood, and conditional probability;
- optimization basics, especially gradient descent;
- train/validation/test splits, loss functions, overfitting, regularization, and evaluation;
- Python and NumPy.

## Track structure

### 01 — Neural Network Foundations

Learn what neural networks are before treating them as frameworks.

- biological inspiration versus mathematical reality;
- perceptron and linear threshold units;
- neurons as affine transformations followed by nonlinearities;
- multilayer perceptrons;
- computational graphs;
- forward propagation;
- activation functions: sigmoid, tanh, ReLU, Leaky ReLU, GELU, SiLU/Swish;
- output layers for regression, binary classification, multiclass classification, and multilabel prediction;
- common loss functions;
- universal approximation intuition;
- parameter counting and tensor shapes;
- representation learning intuition.

### 02 — Training Neural Networks

Understand how neural networks actually learn.

- empirical risk minimization;
- backpropagation from first principles;
- computational differentiation;
- numerical versus analytical gradients;
- gradient checking;
- full-batch, stochastic, and mini-batch gradient descent;
- momentum and Nesterov acceleration;
- AdaGrad, RMSProp, Adam, AdamW;
- learning-rate selection;
- warm-up and learning-rate schedules;
- vanishing and exploding gradients;
- initialization: zero, random, Xavier/Glorot, He/Kaiming;
- gradient clipping;
- batch size and optimization noise;
- convergence diagnostics.

### 03 — Generalization, Regularization & Training Stability

Learn why low training loss does not imply a useful model.

- bias/variance in deep models;
- L1/L2 regularization and weight decay;
- dropout;
- early stopping;
- data augmentation;
- label smoothing;
- batch normalization;
- layer normalization;
- group and instance normalization;
- residual connections;
- normalization versus initialization;
- calibration and confidence;
- class imbalance;
- noisy labels;
- hyperparameter search;
- scaling behavior and capacity.

### 04 — Core Deep Learning Architectures

Study the architectural ideas that became building blocks for modern AI.

- deep feed-forward networks;
- convolutional neural networks;
- convolution, padding, stride, dilation, pooling, and receptive fields;
- canonical CNN evolution: LeNet, AlexNet, VGG, Inception, ResNet, DenseNet;
- recurrent neural networks;
- backpropagation through time;
- LSTM and GRU;
- sequence-to-sequence models;
- encoder-decoder architectures;
- attention mechanisms;
- self-attention and cross-attention;
- positional representations;
- transformers;
- encoder-only, decoder-only, and encoder-decoder transformers;
- mixture-of-experts fundamentals;
- graph neural network fundamentals;
- memory and state-space architectures as advanced extensions.

> CNNs, RNNs, attention, and transformers are explained canonically here. The CV and NLP tracks should focus on domain-specific use rather than duplicate the mathematical foundations.

### 05 — Generative Deep Learning

Learn the major paradigms for learning and sampling complex data distributions.

- latent-variable models;
- autoencoders;
- denoising and sparse autoencoders;
- variational autoencoders;
- autoregressive modeling;
- generative adversarial networks;
- diffusion and score-based models;
- normalizing-flow intuition;
- energy-based model intuition;
- conditioning and classifier-free guidance;
- representation versus generation;
- likelihood-based versus implicit generative models.

### 06 — Practical Deep Learning

Turn mathematical understanding into reliable engineering practice.

- PyTorch fundamentals;
- TensorFlow/Keras fundamentals;
- tensors, autograd, modules, datasets, dataloaders, and training loops;
- writing a model without high-level training abstractions;
- GPU/accelerator fundamentals;
- memory estimation;
- mixed-precision training;
- gradient accumulation;
- checkpointing and reproducibility;
- experiment tracking;
- profiling bottlenecks;
- debugging NaNs, dead activations, bad gradients, and data pipelines;
- transfer learning and fine-tuning;
- parameter-efficient fine-tuning fundamentals;
- distributed training concepts;
- inference optimization fundamentals;
- exporting and serving neural networks.

## Suggested progression

```text
Perceptron
   ↓
MLP + activations + losses
   ↓
Forward propagation
   ↓
Backpropagation
   ↓
Optimization + initialization
   ↓
Regularization + normalization
   ↓
Deep architectures
   ├── CNN ───────────────→ Computer Vision
   ├── RNN / LSTM ───────→ Sequence Modeling
   ├── Attention
   │      ↓
   │   Transformer ──────→ NLP / LLMs / Multimodal
   └── Generative Models → Generative AI
```

## Minimum completion standard

A learner completing the core of this track should be able to:

1. implement a small neural network and backpropagation using NumPy;
2. derive gradients for a simple multilayer network;
3. explain the role of nonlinear activation functions;
4. diagnose vanishing/exploding gradients and overfitting;
5. train an equivalent model in a deep-learning framework;
6. compare optimizers, initialization strategies, and regularizers experimentally;
7. explain CNNs, recurrent networks, attention, and transformers at the level of tensor operations;
8. distinguish discriminative and major generative modeling paradigms;
9. reason about training compute, memory, data, and inference constraints;
10. identify when deep learning is unnecessary and a simpler method is preferable.

## Relationship to other tracks

- **Computer Vision** depends heavily on CNNs, vision transformers, augmentation, transfer learning, and multimodal representation learning.
- **Natural Language Processing** depends on embeddings, sequence modeling, attention, transformers, and language modeling.
- **Reinforcement Learning** reuses neural networks for function approximation, policies, critics, and world models.
- **Advanced AI Systems** builds on transformers, generative models, fine-tuning, retrieval, evaluation, agents, multimodal systems, and scalable inference.
