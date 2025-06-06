# Continuous Control with Deep Reinforcement Learning (DDPG)

> **Reimplementation of**:  
> 📄 *Continuous Control with Deep Reinforcement Learning*,  
> by Timothy P. Lillicrap\*, Jonathan J. Hunt\*, Alexander Pritzel, Nicolas Heess, Tom Erez, Yuval Tassa, David Silver & Daan Wierstra  
> 📍 Published at **ICLR 2016** — [arXiv:1509.02971](https://arxiv.org/abs/1509.02971)

---

## 📌 Overview

This repository contains a PyTorch reimplementation of the **Deep Deterministic Policy Gradient (DDPG)** algorithm, which extends Deep Q-Learning to continuous control problems.

DDPG is a model-free, off-policy actor-critic algorithm that can learn policies in high-dimensional, continuous action spaces.

---

## 🛠️ Features

- ✅ Fully modular PyTorch implementation  
- ✅ Works with any OpenAI Gym continuous control environment  
- ✅ Actor-Critic with target networks  
- ✅ Experience Replay  
- ✅ Ornstein–Uhlenbeck noise for exploration  
- ✅ TensorBoard logging support

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<your_username>/ddpg-pytorch.git
cd ddpg-pytorch
