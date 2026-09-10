# Classical ML Models from Scratch

> Implementing foundational machine learning algorithms from the ground up — no sklearn, just math and Python.

---

## Overview

This project is a hands-on deep dive into the core algorithms that power modern machine learning. Each model is built from scratch using only Python and numerical libraries (NumPy), with the goal of demonstrating a thorough understanding of the underlying mathematics — not just API usage.

This is distinct from simply calling `sklearn.fit()`. Every forward pass, gradient computation, and convergence check is written explicitly and intentionally.

---

## Models Implemented

### Supervised Learning

| Model | Type | Key Concepts |
|---|---|---|
| **Linear Regression** | Regression | Least squares, gradient descent, MSE loss |
| **Logistic Regression** | Classification | Sigmoid activation, log loss, binary cross-entropy |

### Unsupervised Learning

| Model | Type | Key Concepts |
|---|---|---|
| **K-Means Clustering** | Clustering | Centroid initialization, Euclidean distance, iterative convergence |

---

## Why Build From Scratch?

- i felt as though using libraries for certain algorithms was not enough to make me feel   comfortable using them so this is the first of a series of me trying to figure out how ml models work under the hood from first principles

- **Reveals the math** behind things like gradient descent and decision boundaries
- **Forces precision** — you can't guess at what a parameter does when you have to implement it yourself
- **Demonstrates depth** to engineers and teams evaluating your skills

---

## Project Structure

```
classical-ml-models-from-scratch/
│
├── linear regression/          # Linear regression implementation
├── logistic regression model/  # Binary classifier with sigmoid + log loss
├── unsupervised learning/
│   └── k-mean/                 # K-Means clustering
│
├── pyproject.toml              # Project config & dependencies
└── .python-version             # Pinned Python version
```

---

## Tech Stack

- **Python** (version pinned via `.python-version`)
- **NumPy** — vectorised math operations
- **Matplotlib** — visualisation (where applicable)

---

## Getting Started

```bash
# Clone the repo
git clone https://github.com/genericmaster/classical-ml-models-from-scratch.git
cd classical-ml-models-from-scratch

# Install dependencies
pip install .
# or, if using uv:
uv sync
```

Then navigate into any model folder and run the notebook or script inside.

---

## Roadmap

Planned additions:

- [ ] Decision Tree
- [ ] Naive Bayes
- [ ] Principal Component Analysis (PCA)
- [ ] Support Vector Machine (SVM)
- [ ] K-Nearest Neighbours (KNN)

---
- a look into building deep learning models from scratch as well

## About

Built as part of a machine learning portfolio to demonstrate practical understanding of classical algorithms beyond library usage.


Feel free to explore, fork, or reach out with questions.