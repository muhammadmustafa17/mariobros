# AI Super Mario Bros Agent Using Deep Reinforcement Learning

## Overview

This project implements an **Artificial Intelligence agent capable of playing Super Mario Bros using Deep Reinforcement Learning**.

The agent learns how to navigate the game environment by interacting with the game, receiving rewards based on its actions, and improving its strategy through trial and error.

The project uses the **Proximal Policy Optimization (PPO)** algorithm with a **CNN-based policy network** to process game frames and learn optimal actions.

This project was developed as part of my Master's program and explores the application of reinforcement learning in game environments.

---

## Features

* AI agent trained to play Super Mario Bros
* Reinforcement learning-based decision making
* Computer vision-based game state processing
* CNN policy network for visual input
* Automated model checkpoint saving
* Real-time agent testing
* Frame stacking for temporal information

---

## Technologies Used

* Python
* PyTorch
* Stable-Baselines3
* OpenAI Gym
* Gym Super Mario Bros
* NES-Py
* TensorBoard
* NumPy
* OpenCV

---

# System Architecture

The workflow of the project:

```
Super Mario Bros Environment
            |
            |
Game Frames / Observations
            |
            |
Image Preprocessing
(Grayscale + Frame Stacking)
            |
            |
CNN Policy Network
            |
            |
PPO Reinforcement Learning Agent
            |
            |
Action Selection
(Move / Jump / Run)
            |
            |
Updated Environment State
```

---

# How It Works

## 1. Game Environment Setup

The Super Mario Bros environment is created using:

* Gym Super Mario Bros
* NES-Py
* Joypad wrapper

The action space is simplified to allow the AI agent to focus on learning essential movements.

Available actions include:

* Move left
* Move right
* Jump
* Run

---

# 2. Environment Preprocessing

To make training efficient, the game frames are processed before being provided to the neural network.

The preprocessing pipeline includes:

### Grayscale Conversion

The RGB game frames are converted into grayscale images to reduce computational complexity.

### Frame Stacking

Multiple consecutive frames are stacked together so the model can understand movement and game dynamics.

Example:

```
Frame 1
Frame 2
Frame 3
Frame 4

      ↓

Combined State Representation
```

---

# 3. Reinforcement Learning Model

The project uses:

## Proximal Policy Optimization (PPO)

PPO is a policy optimization algorithm that improves the agent's actions by learning from previous experiences while maintaining stable training.

The agent learns:

* Which actions maximize rewards
* How to avoid obstacles
* How to progress through levels

---

# Neural Network Architecture

The PPO agent uses a CNN policy:

```
Input:
Game Frame Stack

        ↓

Convolutional Neural Network

        ↓

Feature Extraction

        ↓

Policy Network

        ↓

Action Prediction

        ↓

Mario Movement
```

---

# Training Process

During training:

1. Mario observes the current game state
2. The model selects an action
3. The environment provides:

   * New state
   * Reward
   * Completion status
4. PPO updates the neural network
5. The agent improves over time

---

# Training Configuration

Model:

```
Algorithm:
Proximal Policy Optimization (PPO)

Policy:
CNN Policy

Learning Rate:
0.000001

Training Steps:
1,000,000 timesteps
```

---

# Model Saving

Training checkpoints are automatically saved during training.

The callback system stores the best-performing models so they can be tested later.

Example:

```
train/

├── best_model_1000000
└── checkpoints
```

---

# Testing the AI Agent

After training, the saved model is loaded and tested.

The AI agent:

* Observes the game
* Predicts actions
* Controls Mario automatically
* Plays the game without human input

Example:

```
Input:
Game Screen

Output:
AI chooses:
→ Move right
→ Jump
→ Avoid obstacle
```

---

# Installation

Install required dependencies:

```bash
pip install gym-super-mario-bros
pip install nes-py
pip install stable-baselines3
pip install torch torchvision
pip install gym
```

---

# Running the Project

Open:

```
mariobros.ipynb
```

Run sections in order:

1. Setup Mario environment
2. Preprocess observations
3. Train reinforcement learning model
4. Test trained agent

---

# Results

The trained AI agent learns to:

* Navigate Mario levels
* Select actions based on visual input
* Improve gameplay through reinforcement learning

The project demonstrates how reinforcement learning can be applied to autonomous decision-making systems.

---

# Future Improvements

Possible improvements:

* Train on multiple Mario levels
* Improve exploration strategies
* Use advanced algorithms such as SAC or A3C
* Deploy the model on edge devices
* Add human-vs-AI gameplay comparison
* Optimize inference speed

---

# Author

Muhammad Mustafa

Master's Project
Artificial Intelligence / Machine Learning
