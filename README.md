AMM LP Simulation Dashboard

A quantitative research tool for modeling AMM liquidity provider performance under stochastic price dynamics.
Built with Python, Streamlit, NumPy, and Matplotlib.

🚀 Overview

This project is a full-featured DeFi quantitative simulation framework designed to analyze the risk and return profile of Automated Market Makers (AMMs) across:

Uniswap v2 (constant product AMM)

Uniswap v2 with dynamic fees (volatility-adjusted)

Uniswap v3 (concentrated liquidity)

It includes:

✔ GBM calibration from real historical prices (BTC, ETH, UNI, XRP, S&P500)
✔ LP vs HODL return simulation under different AMM models
✔ Dynamic fee modeling based on realized volatility
✔ Autocorrelation and volatility clustering diagnostics
✔ Rolling volatility visualization
✔ Impermanent loss decomposition
✔ Optimal range search for Uniswap v3 positions
✔ Full interactive visualization with Streamlit

This dashboard mirrors the kind of modeling performed by Gauntlet, Chaos Labs, and other DeFi risk teams.

🧠 Key Questions This Tool Answers
🧩 For Uniswap v2 LPs

Do LPs outperform HODLing under certain market regimes?

How does increased volatility impact expected LP returns?

What is the expected long-term impermanent loss?

⚡ With Dynamic Fees

Can fee multipliers offset impermanent loss?

How much do realized volatility spikes contribute to LP yield?

🎯 For Uniswap v3 Positions

What is the optimal range for maximizing LP/HODL performance?

How frequently does price exit the range?

How does concentrated liquidity affect tail risk?

Mathematical Modeling
1. Price Dynamics (GBM)

Each asset follows:

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


Simulation uses:

Annualized drift (μ)

Annualized volatility (σ)

User-selected path count and horizon (T)

Historical calibration uses daily log returns:

𝜇
=
mean(returns)
×
365
,
𝜎
=
std(returns)
×
365
μ=mean(returns)×365,σ=std(returns)×
365
	​

2. Uniswap v2 (constant product)

Invariant:

𝑥
𝑦
=
𝑘
xy=k

LP value at time 
𝑡
t:

𝑉
𝐿
𝑃
(
𝑡
)
=
2
𝑥
𝑡
𝑦
𝑡
V
LP
	​

(t)=2
x
t
	​

y
t
	​

	​


Impermanent loss:

𝐼
𝐿
=
2
𝑃
1
+
𝑃
−
1
IL=
1+P
2
P
	​

	​

−1
3. Dynamic Fee Model (Volatility-Adjusted)

Fees scale with realized volatility:

𝑓
𝑡
=
𝑓
0
+
𝛼
⋅
RealizedVol
𝑡
f
t
	​

=f
0
	​

+α⋅RealizedVol
t
	​


Captures empirical behavior of DEXs under high-volatility periods

Allows LPs to earn more during large price swings

4. Uniswap v3 (Concentrated Liquidity)

LP value only accrues inside chosen price range 
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
Outside range, LP becomes fully one-sided.

The simulation tracks:

Time spent in-range vs out-of-range

Range exit frequency

LP/HODL relative value

🧰 Features
✔ Real Data Calibration

BTC, ETH, UNI, XRP, S&P500

OHLC cleaned & resampled

GBM drift & volatility estimation

Rolling volatility (21-day window)

ACF of returns and squared returns

Detects volatility clustering

✔ LP Simulation Modules
Model	Supported
Uniswap v2 (constant fees)	✅
Uniswap v2 (dynamic fees)	✅
Uniswap v3 (concentrated liquidity)	✅
Arbitrary price paths (user-defined)	🟡 optional

Outputs include:

LP portfolio value

HODL benchmark

LP/HODL ratio distribution

Impermanent loss

Fee income

Return decomposition

✔ Uniswap v3 Optimal Range Search

Grid search over:

Lower bound range

Upper bound range

Grid resolution

Returns top-performing ranges by mean LP/HODL.
