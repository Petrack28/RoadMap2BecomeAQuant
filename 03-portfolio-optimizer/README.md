# Portfolio Optimizer (Markowitz, Max-Sharpe)

> Status: ✅ Done

## Problem

Given a set of assets, what allocation minimizes risk for a target return, and what allocation maximizes risk-adjusted return (Sharpe ratio)? This project implements Markowitz mean-variance optimization as an interactive Streamlit app: the user inputs any list of tickers, a date range, and a risk-free rate, and the app computes the efficient frontier, the Global Minimum Variance (GMV) portfolio, and the Maximum Sharpe portfolio in real time.

## Data

- Daily closing prices via `yfinance`, user-configurable tickers and date range
- Log returns computed as `log(P(t)/P(t-1))`
- Expected returns (μ) and covariance matrix (Σ) annualized (×252, ×√252)

## Method

1. **Optimization:** `scipy.optimize.minimize` (SLSQP) with the constraint that weights sum to 1 and are non-negative (long-only)
2. **Efficient frontier:** for 50 target returns spanning the asset universe, minimize portfolio variance subject to that target return
3. **GMV portfolio:** minimize variance with no return constraint
4. **Max-Sharpe portfolio:** maximize `(return - risk_free) / volatility`
5. **Critical engineering detail:** ticker order is always derived from `returns.columns.tolist()` *after* downloading data, never assumed from user input — `yfinance` can silently reorder columns alphabetically, which previously caused a serious silent bug (TSLA/GLD swapped) in an earlier version of this analysis

## Results

- With AAPL/TSLA/AMZN/GLD (2020-2024), the Max-Sharpe portfolio allocates ~51% GLD / ~20% TSLA / ~29% AAPL / 0% AMZN — GLD and TSLA sit at the two extremes of the efficient frontier (min-risk and max-return respectively), while AMZN is dominated (strictly worse risk/return than achievable combinations) and receives zero weight
- **Stress-test finding:** when tested on a 7-stock tech universe (AAPL, AMD, AMZN, META, MSFT, NVDA, TSLA) over a short, sharply negative 2026 Q1 window, the Max-Sharpe and GMV portfolios diverge sharply in behavior — Max-Sharpe concentrates 100% in the single "least-bad" asset (AMD), while GMV still diversifies across multiple assets (AAPL 51.6%, MSFT 25.2%, AMZN 11.6%, etc.) despite MSFT having the worst individual return — because GMV optimizes purely for risk reduction via correlation structure, independent of return ranking
- This confirms a key Markowitz principle hands-on: minimum-variance allocation depends on the covariance structure, not on each asset's standalone quality

## Limitations

- Long-only (no short selling) — real Sharpe-maximizing portfolios in practice often use leverage or shorts, not modeled here
- Annualizing short windows (e.g., 3 months) amplifies returns/volatility numbers dramatically and can produce misleading "annualized" figures — a known and demonstrated pitfall of this app when used with short date ranges
- No transaction costs, rebalancing logic, or estimation-error correction (Markowitz weights are notoriously sensitive to small changes in μ — this is the textbook version, not a production-grade robust optimizer)
- Risk-free rate is a single user-set constant, not pulled from real market data (e.g., T-bill rates)