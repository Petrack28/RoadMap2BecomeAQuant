# Walk-Forward Validation & Robustness

> Status: ✅ Done

## Problem

A trading hypothesis (London Breakout: Asian-session range breakout with wick-then-body retest confirmation) is only credible if it survives out-of-sample validation, not just an in-sample backtest. This project implements the strategy independently in both Pine Script and Python, cross-verifies the two implementations, and applies statistical significance testing plus walk-forward analysis to determine whether any apparent edge is real or noise.

## Data

- **Pine Script:** EUR/USD, 1H candles, ~3.5 years (OANDA feed via TradingView), no commission/slippage modeled
- **Python:** EUR/USD, 1H candles, ~6 months (`yfinance` — intraday history is capped by the API's rolling window, which is shorter than initially assumed and was discovered empirically)

## Method

1. **Strategy design (bottom-up, not copied):** Asian session range (00:00-08:00 UTC) → breakout defined by candle **close** beyond the range (not wick, to reduce false breakouts) → entry only after a wick retest of the broken level followed by a confirming close in the breakout direction (OCO logic implicit: only one direction active per day)
2. **Dual independent implementation:** built the logic first as language-agnostic pseudocode, then in Pine Script v6, then replicated independently in Python — used as a cross-check, not just for convenience
3. **Bug discovery via cross-verification:** the Python replication initially used timestamps in `Europe/London` timezone without conversion to UTC — an easy-to-miss silent bug (same class of error as the earlier ticker-ordering bug in Week 1) caught only because results were being compared against the Pine Script run
4. **Statistical significance:** one-sample t-test on trade-level returns (H0: mean return = 0), analogous to the alpha-significance test used in Week 3's CAPM regression
5. **Walk-forward split:** trades ordered chronologically, first 70% (training) vs last 30% (testing) — explicitly NOT a random split, to avoid lookahead bias in the validation process itself
6. **Multiple-testing framing:** quantified why "trying more parameter combinations until one looks good" is dangerous — with 90 combinations tested at a 5% significance threshold, P(at least one false positive) ≈ 99.81%, even if none have real edge

## Results

| Test | Result |
|---|---|
| Pine Script backtest (444 trades, 3.5yr) | Sharpe -1.13, Profit Factor 1.01, PnL +0.08% |
| Python backtest (85 trades, 6mo) | Mean return -0.0139%/trade |
| One-sample t-test on Python trades | t-stat modest, **p=0.60** — not significant |
| Walk-forward: train (59 trades) | Mean return +0.0007% (~neutral) |
| Walk-forward: test (26 trades) | Mean return -0.0469% (worse than train) |

- Two independent implementations, two different time periods, converge on the same conclusion: **no statistically defensible edge** for this strategy in its current form
- The train/test divergence (near-zero vs clearly negative) is the classic signature of a strategy that does not generalize — though the out-of-sample sample size (26 trades) is itself too small to make this claim with full statistical confidence, an honest limitation rather than a false claim of certainty
- This is treated as a valid, complete research finding: a negative, well-documented result is as much a portfolio deliverable as a positive one

## Limitations

- Python backtest period (6 months) is much shorter than the Pine Script period (3.5 years) due to `yfinance` intraday data limits — the two are complementary evidence, not a like-for-like comparison
- No transaction costs modeled in either implementation (commission was left at 0 in Pine Script by design, to isolate the raw signal first) — real-world costs would only make the result worse, never better
- Exit rule (close of day) was a simplification, not derived from the original strategy design — a stop-loss/take-profit-based exit was not tested and could change results materially
- Walk-forward here is a single 70/30 split, not a rolling/anchored walk-forward across multiple windows (a more robust version for future work)
- IFVG (the second hypothesis from the trading research track) was deferred and not yet tested with this same rigor — pending for a future session