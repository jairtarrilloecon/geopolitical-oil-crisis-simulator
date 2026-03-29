<div align="center">
  <b>🌍 Languages / Idiomas:</b><br>
  <a href="#-english">🇺🇸 English</a> | <a href="#-español">🇪🇸 Español</a>
</div>

---

## 🇺🇸 English

# Geopolitical Oil Market Simulator 🛢️🌐
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jairtarrilloecon/geopolitical-oil-crisis-simulator/main?urlpath=voila%2Frender%2F02_simulador_mercado_petroleo.ipynb)

**A Python-based macroeconomic model predicting global crude oil price shocks driven by geopolitical disruptions in the Strait of Hormuz.**

> Designed to simulate the economic consequences of a NATO-Iran naval conflict on the global energy supply chain.

### 📌 Project Overview
The global economy operates on an inelastic demand for crude oil (~104.8 mb/d). Over 20% of this demand (20.9 mb/d) funnels strictly through the Strait of Hormuz. This interactive Python simulator models a mathematical supply-demand curve and calculates the catastrophic real-time impact on crude spot prices (Brent/WTI) when War Risk Premiums trigger a supply breakdown.

#### Key Features
- **Object-Oriented Economic Engine:** Custom-built Python class `MercadoLineal` for algebraic equilibrium solving.
- **Consumer/Producer Surplus Calculation:** Measures the exact value of welfare generated/destroyed under different scenarios.
- **Interactive MLOps Dashboard (ipywidgets):** Allows real-time dragging of conflict variables (e.g., *Strait Closure Risk*) to trigger live "Global Blackout" alerts and dynamic hyperinflation tracking on a Cyber-Economics Dark Theme layout.

### 🛠️ Tech Stack
- **Language:** Python 3.14
- **Core Libraries:** `NumPy`, `Pandas`
- **Frontend / DataViz:** `Matplotlib`, `Seaborn`, `ipywidgets`
- **Environment:** Jupyter Notebooks

### ⚙️ How to Run Locally
1. Clone the repository.
2. Initialize virtual environment (`.venv`) and install dependencies from `requirements.txt`.
3. Open `notebooks/02_simulador_mercado_petroleo.ipynb` and execute all cells.

---

## 🇪🇸 Español

# Simulador de Crisis Petrolera Geopolítica 🛢️🌐
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jairtarrilloecon/geopolitical-oil-crisis-simulator/main?urlpath=voila%2Frender%2F02_simulador_mercado_petroleo.ipynb)

**Un modelo macroeconómico en Python para predecir shocks en el precio global del crudo generados por interrupciones en el Estrecho de Ormuz.**

> Diseñado para simular las consecuencias económicas de un conflicto naval Irán-OTAN en la cadena de suministro energético mundial.

### 📌 Resumen del Proyecto
La economía global depende de una demanda inelástica de crudo (~104.8 mb/d). Más del 20% de esta demanda (20.9 mb/d) transita obligatoriamente por el Estrecho de Ormuz. Este simulador en Python modela matemáticamente el cruce de curvas de Oferta y Demanda para calcular el impacto catastrófico en tiempo real que tendrían las pólizas de "Riesgo de Guerra" sobre el precio spot del barril (Brent/WTI).

#### Funciones Clave
- **Motor Económico Orientado a Objetos:** Clase `MercadoLineal` diseñada para resolver balances algebraicos de sistemas lineales.
- **Medición de Excedentes:** Calcula matemáticamente el triángulo de valor social tanto para el Consumidor como para el Productor.
- **Dashboard MLOps Interactivo:** Interfaz basada en `ipywidgets` que permite arrastrar deslizadores de riesgo geopolítico para detonar alertas rojas y trazar gráficamente la hiperinflación en un entorno oscuro tipo "Terminal de Wall Street". 

### 🛠️ Tecnologías Empleadas
- **Lenguaje:** Python 3.14
- **Librerías Core:** `NumPy`, `Pandas`
- **Visualización:** `Matplotlib`, `Seaborn`, `ipywidgets`
- **Entorno:** Cuadernos de Jupyter (Notebooks)

### ⚙️ Cómo ejecutar el simulador
1. Clona el repositorio en tu máquina.
2. Activa tu entorno virtual (`.venv`) e instala los paquetes desde `requirements.txt`.
3. Abre el archivo `notebooks/02_simulador_mercado_petroleo.ipynb` y ejecuta todo el código.
