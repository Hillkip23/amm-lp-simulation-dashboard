<p align="center">

  <!-- Project Title -->
  <h1 align="center">AMM LP Simulation Dashboard</h1>
  <h4 align="center">Quantitative AMM Risk Modeling • Uniswap v2/v3 • LP Performance Simulation</h4>

  <!-- Live App Badge -->
  <a href="https://amm-lp-simulation-dashboard-gzdftxeqlbiqxtuzbpc3eh.streamlit.app/">
    <img src="https://img.shields.io/badge/Launch_App-Streamlit-FF4B4B?logo=streamlit&logoColor=white" alt="Launch Streamlit App" />
  </a>

  <!-- GitHub Badges -->
  <br/>
  <img src="https://img.shields.io/github/languages/top/Hillkip23/amm-lp-simulation-dashboard?color=blue" alt="Top Language" />
  <img src="https://img.shields.io/github/repo-size/Hillkip23/amm-lp-simulation-dashboard?color=informational" alt="Repo Size" />
  <img src="https://img.shields.io/badge/Python-3.10+-yellow?logo=python" alt="Python Version" />
  <img src="https://img.shields.io/badge/Streamlit-1.x-FF4B4B

AMM LP Simulation Dashboard

A quantitative research platform for modeling AMM liquidity provider performance under stochastic price dynamics.

This Streamlit dashboard analyzes LP returns, impermanent loss, dynamic fees, volatility regimes, and concentrated liquidity performance using Monte Carlo simulations and real-market calibration.

Built with Python, Streamlit, NumPy, and Matplotlib.
Streamlit: https://amm-lp-simulation-dashboard-gzdftxeqlbiqxtuzbpc3eh.streamlit.app/

Project Overview

The AMM LP Simulation Dashboard is a full-featured DeFi quantitative research tool designed to study:

Liquidity provider outcomes across Uniswap v2 and Uniswap v3

LP vs HODL performance under various market regimes

The impact of impermanent loss, fees, and volatility

How concentrated liquidity ranges affect risk & return

How real-world crypto assets behave statistically (drift, volatility, clustering)

This tool mirrors analyses performed by Gauntlet, Chaos Labs, Block Analitica, and academic DeFi research groups.


🧠 Core Features
🔷 1. LP Performance Simulation (Uniswap v2)

Thousands of GBM price paths (Monte Carlo)

Tracks:

LP/HODL ratio

Impermanent loss (IL)

Fee income contribution

Total LP excess return

Histogram, distribution statistics, and path visualizer

Stress scenario engine (bull, bear, crab markets)


🔷 2. Dynamic Fee Modeling

Model the effect of volatility-linked fees:

fee_APR
(
𝑡
)
=
baseFee
+
𝛼
⋅
RealizedVol
(
𝑡
)
fee_APR(t)=baseFee+α⋅RealizedVol(t)

Higher volatility → higher fees → partial IL mitigation.

🔷 3. Real-Market Calibration

Upload or load built-in data for:

BTC

ETH

UNI

XRP

S&P500

The system performs:

Daily log-return extraction

Estimation of annualized drift (μ) and volatility (σ)

Return distribution visualization

Rolling volatility analysis

Autocorrelation of returns

Autocorrelation of squared returns (volatility clustering)

These calibrated parameters can be applied directly to the Monte Carlo engine.


🔷 4. Uniswap v3 Concentrated Liquidity Modeling

Simulate v3 LP returns using user-defined ranges:

Choose lower and upper price bounds

Compute LP payoff at terminal price

Track:

Time spent in-range

Out-of-range behavior

Effects of volatility on range efficiency


🔷 5. Optimal Range Search (Uniswap v3)

A full grid search identifies the best price ranges for LP profitability:

Evaluates mean LP/HODL for each range pair

Produces top-performing 10 ranges

Useful for strategy design and backtesting concentrated liquidity positions

🔷 6. Single Path Visualizer

Pick any simulated path and see:

Price trajectory

LP vs HODL over time

Impermanent loss curve

Helps illustrate how IL evolves throughout volatile markets.


📚 Underlying Models
📉 1. Geometric Brownian Motion (GBM)

Price evolution:

𝑑
𝑆
𝑡
=
𝜇
𝑆
𝑡
𝑑
𝑡
+
𝜎
𝑆
𝑡
𝑑
𝑊
𝑡
dS
t
	​

=μS
t
	​

dt+σS
t
	​

dW
t
	​


Simulated with:
S[t+1] = S[t] * exp((mu - 0.5 * sigma**2)*dt + sigma * sqrt(dt) * Z)

💧 2. Uniswap v2 AMM Model

Invariant:

𝑥
⋅
𝑦
=
𝑘
x⋅y=k

Impermanent loss:

𝐼
𝐿
=
2
𝑃
/
𝑃
0
(
1
+
𝑃
/
𝑃
0
)
−
1
IL=
(1+P/P
0
	​

)
2
P/P
0
	​

	​

	​

−1

📏 3. Uniswap v3 Range Model

LP liquidity is active only within 
[
𝑃
𝐿
,
𝑃
𝑈
]
[P
L
	​

,P
U
	​

].

Outside the range:

Position converts to single-sided exposure

Fee income stops

Range exit frequency affects expected returns






🧰 Features
✔ Real Data Calibration

BTC, ETH, UNI, XRP, S&P500

OHLC cleaned & resampled

GBM drift & volatility estimation

Rolling volatility (21-day window)

ACF of returns and squared returns

Detects volatility clustering

| Model                                | Supported   |
| ------------------------------------ | ----------- |
| Uniswap v2 (constant fees)           | ✅          |
| Uniswap v2 (dynamic fees)            | ✅          |
| Uniswap v3 (concentrated liquidity)  | ✅          |
| Arbitrary price paths (user-defined) | 🟡 optional |


Outputs include:

LP portfolio value

HODL benchmark

LP/HODL ratio distribution

Impermanent loss

Fee income

Return decomposition

Uniswap v3 Optimal Range Search

Grid search over:

Lower bound range

Upper bound range

Grid resolution

Returns top-performing ranges by mean LP/HODL.


