# 📈 RoadMap2BecomeAQuant

My 6-month structured journey from biomedical signal processing (M.Sc. research at CINVESTAV) to quantitative finance. This repository contains everything I learn and build along the way: notes, 13 hands-on projects, and trading systems — from rigorous backtesting to live paper-trading bots.

> **Why this transition makes sense:** my thesis applies fractal analysis (DFA, Hurst exponent), digital filtering, and statistical inference to physiological time series. Financial time series are analyzed with the *same mathematical toolbox* — different signal, same discipline.

📍 **Full roadmap:** [docs/roadmap.md](docs/roadmap.md) · **Class log:** [docs/class-log.md](docs/class-log.md)

---

## 🗂️ Project Portfolio

| # | Project | Topic | Status |
|---|---------|-------|--------|
| 01 | [Factor Analysis](01-factor-analysis/) | CAPM / Fama-French regression | 🔜 Planned |
| 02 | [Quant EDA + Hurst](02-quant-eda-hurst/) | Stylized facts, DFA → Hurst exponent |  ✅  |
| 03 | [Portfolio Optimizer](03-portfolio-optimizer/) | Markowitz, max-Sharpe (Streamlit app) | 🔜 Planned |
| 04 | [Monte Carlo Risk](04-monte-carlo-risk/) | Equity simulation, Kelly sizing | 🔜 Planned |
| 05 | [Backtesting Engine](05-backtesting-engine/) | backtesting.py, full metrics report | 🔜 Planned |
| 06 | [Python ↔ Pine Script](06-python-vs-pinescript/) | Same strategy, two platforms | 🔜 Planned |
| 07 | [Walk-Forward Validation](07-walk-forward-validation/) | Robustness, overfitting detection | 🔜 Planned |
| 08 | [Pairs Trading](08-pairs-trading/) | Cointegration, statistical arbitrage | 🔜 Planned |
| 09 | [Options Pricer](09-options-pricer/) | Black-Scholes, Monte Carlo, binomial, IV | 🔜 Planned |
| 10 | [ML Strategy](10-ml-strategy/) | Triple-barrier labels, purged CV | 🔜 Planned |
| 11 | [Black-Scholes in C++](11-black-scholes-cpp/) | Performance benchmark vs Python | 🔜 Planned |
| 12 | [Paper-Trading Bot](12-paper-trading-bot/) | Autonomous execution, risk controls | 🔜 Planned |
| 13 | [Capstone](13-capstone/) | End-to-end research project | 🔜 Planned |

*Status legend: 🔜 Planned · 🚧 In progress · ✅ Done*

---

## 🛠️ Stack

`Python` · `NumPy / Pandas / SciPy / statsmodels` · `backtesting.py / vectorbt` · `Pine Script v6 (TradingView)` · `scikit-learn / XGBoost` · `Streamlit` · `SQLite` · `C++` · `QuantConnect (LEAN)`

## 📐 Quality standard

Every project README follows the same research structure: **Problem → Data → Method → Results → Limitations.** Honest out-of-sample results over pretty in-sample curves, always.

## ⚠️ Disclaimer

Educational repository. Nothing here is financial advice, and no real money is traded during this roadmap — paper trading only.
