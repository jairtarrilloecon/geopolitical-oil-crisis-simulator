# Geopolitical Oil Market Simulator 🛢️🌐

**A Python-based macroeconomic model predicting global crude oil price shocks driven by geopolitical disruptions in the Strait of Hormuz.**

> Designed to simulate the economic consequences of a NATO-Iran naval conflict on the global energy supply chain.

## 📌 Project Overview
The global economy operates on an inelastic demand for crude oil (~104.8 mb/d). Over 20% of this demand (20.9 mb/d) funnels strictly through the Strait of Hormuz. This interactive Python simulator models a mathematical supply-demand curve and calculates the catastrophic real-time impact on crude spot prices (Brent/WTI) when War Risk Premiums trigger a supply breakdown.

### Key Features
- **Object-Oriented Economic Engine:** Custom-built Python class `MercadoLineal` for algebraic equilibrium solving.
- **Consumer/Producer Surplus Calculation:** Measures the exact value of welfare generated/destroyed under different scenarios.
- **Interactive MLOps Dashboard (ipywidgets):** Allows real-time dragging of conflict variables (e.g., *Strait Closure Risk*) to trigger live "Global Blackout" alerts and dynamic hyperinflation tracking on a Cyber-Economics Dark Theme layout.

## 🛠️ Tech Stack
- **Language:** Python 3.14
- **Core Libraries:** `NumPy`
- **Frontend / DataViz:** `Matplotlib`, `Seaborn`, `ipywidgets`
- **Environment:** Jupyter Notebooks

## ⚙️ How to Run Locally
1. Clone the repository.
2. Navigate to the project folder and map your virtual environment.
3. Install dependencies from `requirements.txt`.
4. Open `/notebooks/02_simulador_mercado_petroleo.ipynb` and execute all cells.

## 📈 Author
**Jair Tarrillo Luján**
Data Analyst / Economics Specialist
