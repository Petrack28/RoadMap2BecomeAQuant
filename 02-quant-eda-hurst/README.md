# Quantitative EDA + Hurst Exponent (DFA)

> Status: ✅ Done

## Problem

Before designing any trading strategy, a quant needs to answer a foundational question: **does this asset's price behave like a random walk (efficient market), or does it have exploitable structure (memory)?** This project performs a rigorous exploratory analysis of TSLA daily returns to characterize their statistical properties — distribution shape, stationarity, volatility memory, and long-range dependence — using the same fractal-analysis toolbox (DFA) applied to physiological time series in my M.Sc. thesis on fNIRS signal processing.

## Data

- **Asset:** TSLA daily closing prices, 2020-01-01 to 2024-12-31 (source: Yahoo Finance via `yfinance`)
- **Transform:** log returns `r(t) = log(P(t)/P(t-1))`, used instead of simple returns for time-additivity and direct correspondence with Geometric Brownian Motion

## Method

1. **Descriptive statistics:** mean, std, skewness, excess kurtosis (annualized return/volatility)
2. **Distribution fit:** histogram vs Normal, QQ-plot, Shapiro-Wilk normality test, t-Student MLE fit (degrees of freedom ν) to quantify fat tails
3. **Stationarity:** Augmented Dickey-Fuller test on price level vs log returns
4. **Memory structure:** ACF/PACF on returns (directional memory) vs squared returns (volatility memory/clustering)
5. **Long-range dependence:** Hurst exponent via Detrended Fluctuation Analysis (DFA) — log-log regression of RMS fluctuation vs window scale, exactly the pipeline used on fNIRS data in my thesis

## Results

- TSLA log returns reject normality (Shapiro-Wilk p < 0.05); excess kurtosis ≈ 3.5–6.5 confirms fat tails
- t-Student fit (ν ≈ 4.2) models tail risk far more accurately than Normal: at -15% daily move, t-Student assigns ~44x the probability the Normal does
- Price series is non-stationary (ADF fails to reject unit root); log returns are stationary (ADF rejects, p < 0.05)
- ACF of raw returns shows little significant autocorrelation (near-random direction), but ACF of squared returns shows strong, persistent autocorrelation in the first 1-15 lags — confirming **volatility clustering**: tomorrow's direction is hard to predict, but tomorrow's volatility magnitude is not
- Hurst exponent H ≈ 0.50 at the daily timeframe (consistent with near-efficient markets), but **H rises to ≈0.63 at the 5-minute intraday timeframe** — though a bootstrap confidence interval [0.40, 0.65] could not reject H=0.5, meaning this apparent intraday trend signal is **not statistically significant** with the sample size available

## Limitations

- Hurst estimates were not validated with a temporally-coherent block bootstrap (a naive i.i.d. bootstrap was used, which is not strictly valid for autocorrelated series — a methodological gap to revisit)
- Single-asset, single-period analysis; results are not necessarily stable across market regimes (e.g., 2020 COVID crash vs 2021 bull run)
- t-Student fit uses unconditional MLE; a time-varying volatility model (GARCH, covered in Month 4) would likely fit the conditional distribution better
- Intraday data limited to 5 trading days (yfinance free tier constraint) — too short to draw firm conclusions about intraday memory
