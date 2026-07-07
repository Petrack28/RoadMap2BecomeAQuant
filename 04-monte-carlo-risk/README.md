# Monte Carlo Risk & Position Sizing

> Status: ✅ Done

## Problem

Given a favorable but uncertain betting/trading edge (win probability p > 0.5), what fraction of capital should be risked per trade to maximize long-term growth without risking ruin? This project implements the Kelly Criterion analytically and validates it via Monte Carlo simulation, quantifying the real trade-off between expected growth and downside risk across different bet-sizing fractions.

## Data

Synthetic simulation (no market data) — a repeated binary bet with:
- Win probability `p = 0.6`
- Payout ratio `b = 1` (double the stake on a win)
- 200 rounds per simulated trajectory, 1,000 independent trajectories per fraction tested

## Method

1. **Kelly Criterion (analytical):** `f* = p - (1-p)/b`, derived from maximizing the expected logarithm of terminal wealth (geometric growth), not expected value directly
2. **Monte Carlo simulation:** simulate 1,000 independent 200-round trajectories for five capital fractions (f = 0.05, 0.20 [Kelly-optimal], 0.40, 0.60, 0.90), applying `capital *= (1 + f·b)` on a win and `capital *= (1 - f)` on a loss
3. **Risk assessment beyond the mean:** for each fraction, compute the median terminal capital *and* the 5th/95th percentiles — the 5th percentile serves the same role here as VaR(95%) does for daily returns (Week 7): it quantifies the adverse tail, not just the central tendency
4. **Full-Kelly vs fractional-Kelly comparison:** explicitly compare f=0.20 (full Kelly) against f=0.05 (a conservative fraction) on both median outcome and worst-case (P5%) outcome

## Results

- With p=0.6 fixed and known exactly over 200 rounds, full Kelly (f=0.20) produces a dramatically higher median terminal capital (~$5,610) than a conservative fraction (f=0.05, ~$576) — confirming Kelly maximizes expected geometric growth when the edge is known and stable
- However, full Kelly's 5th-percentile outcome (~$43) is *worse* than the conservative fraction's 5th percentile (~$173) — in the unlucky 5% of paths, full Kelly loses more than half the starting capital, while the conservative fraction rarely drops below the initial $100
- This quantifies, with simulation rather than folklore, why practitioners use fractional Kelly (typically half-Kelly or less): it sacrifices some expected growth in exchange for materially better worst-case protection
- The practical justification for fractional Kelly is less about f* being "wrong" when p is known exactly, and more about **parameter uncertainty**: real trading edges are estimated from historical data with error, and Kelly sizing computed on an overestimated p can lead to severe over-betting and ruin risk that this experiment (which assumes p is known with certainty) does not capture

## Limitations

- Assumes p is known exactly and constant across all 200 rounds — real trading edges are estimated with uncertainty and typically decay or vary over time (regime changes), which this simulation does not model
- Binary win/lose-all-or-double payout structure is a simplification; real position sizing involves continuous return distributions with fat tails (as established in Week 1-2 of this roadmap), not a fixed binary payout
- No transaction costs or capital constraints (e.g., minimum position size, margin requirements) are modeled
- Does not model correlated bets (sequential trades in a real strategy are rarely independent, unlike this i.i.d. simulation)