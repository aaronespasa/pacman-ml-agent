# Creating Pac-Man Agent using Machine Learning (Classification + Regression)
<p align="center">
  <img src="https://lh3.googleusercontent.com/H8hhcUas7f9Pi4aMLTQfSTVk1wwE1d_SPYYGldXn9S8GARJis2ED4EpnIfXzfBhTP8KZM64bFnmgowpU3Ct7b7OznwcRakNOM3mB2KRr=s660" alt="pac-man banner" />
</p>
  
Welcome to the Pac-Man Agent project! The aim of this project is to create an intelligent Pac-Man agent using machine learning techniques, specifically classification and regression, to predict Pac-Man's actions and future scores. This repository contains all the necessary files and instructions to get started and understand the project.

## Table of Contents
<ol>
<li><a href="#overview">Overview</a></li>
<li><a href="#getting-started">Getting Started</a></li>
<li><a href="#project-structure">Project Structure</a></li>
<li><a href="#methodology">Methodology</a></li>
<li><a href="#results">Results</a></li>
<li><a href="#conclusions">Conclusions and Challenges</a></li>
</ol>

<h2 id="overview">Overview</h2>
This project uses machine learning algorithms to create a Pac-Man agent that can play the game autonomously. The agent's actions are determined using a classification model, and its future score is predicted using a regression model. The main goal of this project is to develop an agent that can achieve a high score by following the optimal path to eat the ghosts while avoiding obstacles.

<h2 id="getting-started">Getting Started</h2>

To get started with the project, follow these steps:

1. Clone the repository to your local machine:
```bash
$ git clone https://github.com/aaronespasa/pacman-ml-agent.git
$ cd pacman-ml-agent
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the project:
```bash
$ python pacman.py
```

<h2 id="project-structure">Project Structure</h2>
The project is organized into the following structure:

```bash
pacman-ml-agent
│
├── RandomAgents.py
├── busters.py
├── bustersAgents.py
├── bustersGhostAgents.py
├── data
│   ├── future
│   ├── present
│   └── raw
├── distanceCalculator.py
├── filterFuture.py
├── filterPresent.py
├── game.py
├── getting_dataset.sh
├── ghostAgents.py
├── grading.py
├── graphicsDisplay.py
├── graphicsUtils.py
├── inference.py
├── keyboardAgents.py
├── layout.py
├── layouts
├── models
│   ├── classification
│   └── prediction
├── pacman.py
├── projectParams.py
├── textDisplay.py
├── util.py
└── wekaI.py
```

<h2 id="methodology">Methodology</h2>
The project methodology involves several stages:

1. Data Collection: Game data is collected using various maps and saved in the .arff format.
2. Data Processing: The raw data is pre-processed and separated into present and future datasets.
3. Model Training: Classification and regression models are trained using the processed data.
4. Model Evaluation: The models are evaluated using the Experimenter in Weka.
5. Model Selection: The best performing models are selected for implementation in the Pac-Man agent.
6. Agent Implementation: The trained models are used to create an autonomous Pac-Man agent.

<h2 id="results">Results</h2>
The project used various machine learning algorithms for classification and regression tasks. The best performing algorithms were:

<ul>
<li>J48</li>
<li>IBK with K = 1</li>
<li>RandomForest</li>
<li>RandomTree</li>
<li>K Star</li>
</ul>

The results were significantly improved (around 6%) after increasing the number of training instances.

<h2 id="conclusion">Conclusions and Challenges</h2>
The main challenge faced during this project was identifying the most relevant attributes for training a generalizable Pac-Man agent. A large number of tests were performed to find the best combination of instances, maps, attributes, training sets, and test sets. Despite the changes, the best performing algorithms remained consistent throughout the experimentation process.

To overcome this challenge, we iteratively refined the feature set and experimented with various machine learning algorithms, eventually settling on a set of features and models that produced an agent with reasonable gameplay behavior. However, there is still room for improvement, and further research could potentially result in a more advanced and adaptable Pac-Man agent.

In conclusion, this project demonstrates the potential of using machine learning techniques to create an autonomous Pac-Man agent. By carefully selecting the features and algorithms, we were able to develop an agent that can achieve a high score in the game. This project serves as a stepping stone for future research and development in the field of game AI and machine learning.
