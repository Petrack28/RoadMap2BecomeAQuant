# Factor Analysis (CAPM / Fama-French)

> Status: ✅ Done

## Problem

Does an asset generate returns beyond what its exposure to the broad market explains (alpha), or is all of its return simply compensation for market risk (beta)? This project implements a CAPM single-factor regression to decompose TSLA, AAPL, and GLD returns into systematic (market-driven) and idiosyncratic components, and tests whether any observed alpha is statistically distinguishable from zero or just noise.

## Data

- Daily closing prices for SPY (market proxy), TSLA, AAPL, GLD — 2020-01-01 to 2024-12-31 (`yfinance`)
- Log returns; market model regressed via OLS (`statsmodels`)

## Method

r_asset(t) = α + β · r_market(t) + ε(t)
- **Beta:** OLS slope coefficient — sensitivity to market moves
- **Alpha:** OLS intercept — excess return unexplained by market exposure
- **R²:** proportion of the asset's variance explained by the market factor
- Statistical significance of alpha assessed via its t-test p-value (H0: α=0)
- Residual normality checked via Jarque-Bera test, cross-validated against excess kurtosis — both confirm fat tails in residuals, consistent with findings throughout this roadmap (OLS's normality assumption is violated, though point estimates remain usable)
- As a complementary inferential exercise, a binomial test (`scipy.stats.binomtest`) was used to illustrate how statistical power scales with sample size: a 70% win rate is not statistically distinguishable from a fair coin at n=20 (p=0.057) but becomes highly significant at n=40 (p=0.0083) — same effect size, different evidentiary strength

## Results

| Ticker | Beta | Alpha (annualized) | Alpha p-value | R² |
|---|---|---|---|---|
| TSLA | 1.626 | +31.89% | 0.217 (not significant) | 0.262 |
| AAPL | 1.190 | +8.95%  | 0.302 (not significant) | 0.628 |
| GLD  | 0.116 | +8.75%  | 0.204 (not significant) | 0.025 |

- None of the three assets show a statistically significant alpha over this 5-year window — the apparent excess returns are not distinguishable from noise at conventional significance levels
- TSLA reacts most strongly to market moves (highest beta) but the market explains the *smallest* share of its total variance (lowest R²) — most of TSLA's movement is idiosyncratic (company-specific news, not macro)
- AAPL is the most market-driven of the three (R²=0.628) despite a more moderate beta — a useful distinction between "how strongly it reacts" (beta) and "how much of its behavior the market explains" (R²)
- GLD is nearly market-independent (R²=0.025, beta≈0.12), consistent with its role as a diversifier established in the Portfolio Optimizer project

## Limitations

- Single-factor CAPM only — no Fama-French size/value/momentum factors, which would likely explain more of AAPL/TSLA's idiosyncratic variance
- 5-year window mixes very different regimes (2020 COVID crash, 2021 bull run, 2022 bear market) without regime-conditioning
- OLS assumes homoscedastic, normal residuals — both violated here (Jarque-Bera rejects normality, kurtosis ≈7); standard errors and p-values may be modestly understated as a result
- Statistical insignificance of alpha does not prove zero true alpha — it means this sample size/period lacks the power to detect it confidently (same caveat demonstrated by the binomial test example)