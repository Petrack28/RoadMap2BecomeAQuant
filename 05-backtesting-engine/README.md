# Backtesting Engine

> Status: ✅ Done

## Problem

Manual backtesting (Week 9) is error-prone and lacks standardized risk metrics. This project formalizes the 50/200 moving-average crossover strategy using `backtesting.py`, a professional-grade vectorized backtesting engine, to generate a complete performance report (Sharpe, Sortino, Calmar, max drawdown, drawdown duration, trade-level statistics) with realistic transaction costs.

## Data

- MSFT daily OHLCV, 2015-01-01 to 2024-12-31 (`yfinance`)
- Commission modeled at 0.1% per trade (a conservative retail-broker approximation)

## Method

1. Strategy class implements the same crossover logic validated manually in Week 9 (50-day MA vs 200-day MA, long-only, no shorting)
2. Cross-validated the engine's internal indicator calculation against an independent manual pandas calculation — confirmed bit-for-bit identical moving averages and exact match on the 4 expected crossover events, ruling out implementation bugs before trusting the report
3. Reconciled `backtesting.py`'s cumulative Return[%] (762.8%) against Week 9's annualized return (21.67%) by converting to an equivalent annualized figure (24.07%, close to the manual estimate after accounting for commissions) — an explicit sanity check that headline "total return" figures are not misread as annualized performance
4. Applied a binomial significance test (as in Week 3) to the strategy's win rate, treating each trade as a Bernoulli trial under a null of no skill (p=0.5)

## Results

| Metric | Value |
|---|---|
| Return (Ann.) | 24.10% |
| Buy & Hold Return | 920.57% (cumulative) — outperformed the strategy |
| Sharpe Ratio | 0.82 |
| Sortino Ratio | 1.53 |
| Calmar Ratio | 0.86 |
| Max. Drawdown | -28.00% (549 days to recover) |
| # Trades | 4 |
| Win Rate | 100% |
| Profit Factor | NaN (no losing trades to divide by) |

- Despite a "perfect" 100% win rate, a binomial test on 4/4 winning trades gives **p=0.062** — just above the conventional 0.05 significance threshold, meaning the result is *not* statistically distinguishable from chance at this sample size
- This directly illustrates the core lesson of Week 9's multiple-testing discussion: an impressive-looking headline metric (100% win rate, 762% return) can coexist with essentially zero statistical confidence when the trade count is this low
- Sortino (1.53) notably exceeds Sharpe (0.82), suggesting a meaningful share of the strategy's volatility comes from large positive moves rather than downside risk — Sharpe's symmetric penalty understates the strategy's risk-adjusted quality on this specific dimension
- Calmar Ratio (0.86) provides the return-per-unit-of-pain framing established in this session's opener: two strategies with identical returns can have very different Calmar ratios, and a strategy with a lower absolute return but far smaller drawdown may be strictly preferable for capital preservation (e.g., prop-firm evaluation accounts with hard drawdown limits)

## Limitations

- Only 4 trades over 10 years — no statistical basis to claim genuine edge; this is a demonstration of the *backtesting methodology*, not a validated trading strategy
- Single asset (MSFT), single parameter set (50/200) — no walk-forward or out-of-sample validation yet (Week 12)
- Commission-only cost model; no bid-ask spread or slippage explicitly modeled (Week 5 concepts not yet integrated into the cost model here)
- Long-only, no short positions — the strategy is fully out of the market ~20% of the time with no downside participation modeled during those periods beyond cash