## Findings from this run

- **Data:** 403 rows, 2025-02-13 to 2026-09-22; latest supplied close **$1,887.04**. All numeric and OHLC structural checks passed. Prices were not independently authenticated.
- **Observed change:** 5,141.8% from the first supplied close to the last, with maximum observed drawdown **-56.5%**. This unusual price range is retained as supplied; adjustment status is unknown.
- **Selection:** **CatBoost** achieved the lowest mean validation origin-normalized RMSE (134.03%) among 8 fixed candidates.
- **Untouched 70-session test:** MAE **$928.65**, RMSE **$1,032.98**, MAPE **62.43%**, R² **-12.072**, random-walk RMSE skill **-1.755**. The selected candidate did not beat the baseline on this test path; this materially weakens confidence in its projection.
- **December 31 point estimate:** **$3,518.95**, a model-implied change of **86.5%** from the snapshot close. This is a conditional model output, not a price target or expected investment return.
- **December 31 simulated envelopes:** nominal 80% **$1,601.99–$7,408.87**; nominal 95% **$1,097.68–$10,703.80**. Historical test path coverage was 51.4% and 85.7% respectively; these are not calibrated future probabilities.

## How to interpret the future projection

The selected model extends relationships estimated from a short and strongly changing historical sample. A rising or falling model path is evidence about that algorithm's extrapolation, not about future earnings, memory demand, valuation or market sentiment. Those inputs are absent here. The no-change baseline remains a useful reference, particularly when test performance is weak. Wide envelopes and disagreement between models express substantial uncertainty. They do not exclude more extreme outcomes.

## What this study cannot establish

This is one ticker, fewer than two years of observations, three validation origins and one untouched test path. Recursive errors accumulate; market regimes and corporate actions can invalidate learned relationships. Price-adjustment settings and exact collection parameters are unknown. Six pre-regular-listing rows are excluded from modeling and included only in the documented sensitivity check. Contemporary correlations and training feature importance do not imply causality. No trading backtest, transaction costs or profitable strategy is claimed.

## Next useful experiments

Verify source values and corporate actions; collect a longer comparable history; add causally available market/sector data; repeat rolling-origin evaluation across more regimes; evaluate direct multi-horizon models; calibrate intervals over many independent forecast origins. Preserve the original test result when designing follow-up experiments.
