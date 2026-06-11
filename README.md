# 2026 FIFA World Cup Predictive AI

> A Stacked Machine Learning Pipeline mapping the physics, geography, and momentum of international football.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![XGBoost](https://img.shields.io/badge/Model-XGBoost-00FF87?logo=xgboost&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## Table of Contents

- [Project Overview](#-project-overview)
- [AI Architecture & Process](#-the-ai-architecture--process)
- [Key Engineered Features](#%EF%B8%8F-key-features-engineered-the-context)
- [Final Tournament Predictions](#-final-tournament-predictions)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Disclaimer](#%EF%B8%8F-disclaimer)
- [License](#-license)
- [Author](#-author)

---

## Project Overview

Most sports prediction models rely solely on historical team rankings (like FIFA or Elo ratings), failing to account for the brutal realities of tournament football. This project takes a completely different approach.

This AI engine simulates the **2026 World Cup** by dynamically quantifying **physical human exhaustion**, **travel fatigue**, **high-altitude physics**, and **opponent-adjusted tactical momentum**. By training a **Stacked XGBoost Ensemble** on over **50,000 historical matches**, the model calculates the exact probability of every fixture and simulates **1,000 "multiverse" tournaments** to find the ultimate World Cup Champion.

A companion **Streamlit dashboard** (`app.py`) presents the model's methodology, team-by-team scouting dossiers, and the full 32-team knockout bracket projection in an interactive, broadcast-style interface.

---

## The AI Architecture & Process

The pipeline is broken down into three distinct operational layers:

### 1. The Elite Feature Engineering Engine (Handling Data Leakage)

To prevent the model from artificially peeking into the future, all historical match data was processed sequentially using a `.shift(1)` strict-time constraint.

- **Dynamic Rest Differential** — Extracted the precise match dates to calculate exact days of rest between games.
- **Exponential Moving Averages (EMA)** — Calculated rolling 10-game tactical momentum, weighing recent matches exponentially higher than past matches.
- **Opponent-Adjusted Form** — Penalized teams for accumulating high-scoring wins against low-tier qualifiers while heavily rewarding teams that generated Expected Goals (xG) against elite defenses.

### 2. The Stacked XGBoost Trainer

Instead of a single predictor, the AI utilizes a multi-layered ensemble approach:

- **Layer 1 — The Expected Goals Engine**
  Two concurrent Gradient Boosted Poisson Regressors (`objective='count:poisson'`). These models act as advanced "Dixon-Coles" calculators, predicting the exact underlying offensive and defensive xG intensity of a given matchup.

- **Layer 2 — The Context Classifier**
  An XGBoost Classifier (`multi:softprob`) that ingests the Elo disparity alongside the physical and tactical context to output a final Win / Draw / Loss probability matrix.

### 3. The Monte Carlo Simulator

Using the official 2026 World Cup Schedule, the script unleashes the trained AI models to simulate the **72-game Group Stage** and **single-elimination knockout brackets 1,000 times**. It aggregates these multiverses to eliminate statistical "flukes" and calculate true advancement equity.

---

## Key Features Engineered (The Context)

Feature importance analysis revealed that raw Elo differences only accounted for **48.5%** of the AI's decision-making. Over **51%** of the predictive power came from engineered contextual variables:

| Feature | Description |
| :--- | :--- |
|  **Physical Exhaustion** (`Rest_Diff`) | The 2026 tournament spans an entire continent. Teams crossing multiple time zones on compressed schedules suffer severe, mathematically quantified penalties in late-game expected goal output. |
|  **Geographic Brutality** (`Altitude`) | Factors in stadium elevation (e.g., the 7,200 ft altitude of Estadio Azteca). European teams unaccustomed to thin air show decreased late-stage efficiency, while host nations receive adaptation multipliers. |
|  **Tactical Momentum** (`Elite_Offense_Diff`) | Adjusts raw win streaks based on the Elo rating of the defeated opponent. |

---

##  Final Tournament Predictions

By running the **Consensus Bracket Generator** (which disables random variance and forces the highest-probability Alpha timeline), the AI predicted the following outcomes:

###  The Alpha Champion: ARGENTINA
Argentina is projected to win back-to-back World Cups. While teams like Spain and England possess similar roster depth, Argentina's metrics show a historically flawless efficiency when converting Expected Goals against elite defensive blocks in high-leverage knockout matches.

###  The Multiverse Winner: SPAIN
In 1,000 randomized Monte Carlo simulations, Spain won the highest overall percentage of tournaments (**34.2%**). Their extreme possession-based system starves opponents of the ball, making them mathematically immune to random "fluke" upsets.

###  The Geographic Victim: GERMANY
The model's most shocking discovery: Germany is mathematically trapped. Despite top-tier player metrics, their schedule projects a Round of 16 collision with host-nation Mexico. The AI calculated that playing at a massive altitude, against a host nation, on 24 hours less rest, is an insurmountable physical bottleneck. **Germany exits early.**

###  The Fallen Giant: BRAZIL
The model severely penalized Brazil due to real-world structural collapses in recent 2026 CONMEBOL qualifiers. **Projected to exit in the Quarterfinals against the highly organized Netherlands.**

---

##  Tech Stack

- **Python 3.10+**
- **XGBoost** — Stacked Poisson Regressors + Multi-class Classifier
- **Pandas / NumPy** — Feature engineering & data processing
- **Streamlit** — Interactive dashboard / front-end
- **Monte Carlo Simulation** — Tournament outcome aggregation

---

##  Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/soumyadeep-rc/fifa-wc-2026-prediction.git
   ```

2. **Create a virtual environment** (recommended)

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

##  Usage

Launch the interactive Streamlit dashboard:

```bash
streamlit run app.py
```

The dashboard includes three sections:

- ** The AI Engine** — model methodology, feature engineering layers, and key statistics
- ** Team Journeys** — squad-by-squad scouting dossiers with win equity, tactical form, and projected bracket paths
- ** The Alpha Bracket** — full Round of 32 → Final knockout projection with the predicted champion

---

##  Project Structure

```
2026-world-cup-predictive-ai/
├── app.py                # Streamlit dashboard
├── requirements.txt      # Python dependencies
├── data/                  # Historical match data
├── models/                # Trained XGBoost ensemble artifacts
├── notebooks/             # Feature engineering & training notebooks
└── README.md
```

---

##  Disclaimer

This project is built for **educational and analytical purposes**. All win probabilities and bracket outcomes are statistical projections generated by a machine learning model — football is a game of fine margins, and real-world results may (and often do) differ from model expectations.

---

##  License

This project is licensed under the [MIT License](LICENSE).

---

##  Author

**Soumyadeep Roy Chowdhury**

Copyright © 2026 Soumyadeep Roy Chowdhury. All rights reserved.
