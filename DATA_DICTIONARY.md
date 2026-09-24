# Data dictionary

## Historical data: `data/sndk_daily_clean.csv`

| Column | Description (1–5 words) | Type | Unit / details |
|---|---|---|---|
| date | Trading session date | date | YYYY-MM-DD; exchange-local date label |
| ticker | Stock ticker symbol | text | SNDK |
| open | Session opening price | float | USD per share, as supplied |
| high | Session highest price | float | USD per share, as supplied |
| low | Session lowest price | float | USD per share, as supplied |
| close | Session closing price | float | USD per share, as supplied |
| volume | Shares traded | integer | Shares, nonnegative |

## Analysis features: `outputs/sndk_analysis_features.csv`

Contains the historical columns above plus:

| Column | Description (1–5 words) | Unit / interpretation |
|---|---|---|
| daily_return_pct | Daily percentage price change | Percent, previous observed close |
| log_return | Daily logarithmic price change | Natural log ratio |
| intraday_range_pct | Intraday percentage price range | Percent of opening price |
| overnight_gap_pct | Opening gap percentage | Percent versus prior close |
| sma_20 | Twenty-session average close | USD, 20-observation trailing window |
| sma_50 | Fifty-session average close | USD, 50-observation trailing window |
| volatility_20_pct | Annualized trailing return volatility | Percent; 20 returns, 252-session convention |
| drawdown_pct | Decline from previous peak | Nonpositive percent |
| volume_ratio_20 | Relative twenty-session volume | Ratio to trailing mean |
| pre_regular_listing | Before regular listing flag | Boolean; date before 2025-02-24 |

Blank initial cells mean insufficient history, not data corruption. These fields are descriptive and available only after the row's close. They must not be used to predict that same close.

## Forecast data: `outputs/sndk_forecast_remaining_2026.csv`

| Column | Description (1–5 words) | Unit / interpretation |
|---|---|---|
| date | Forecast trading session date | ISO date; scheduled session |
| ticker | Stock ticker symbol | SNDK |
| forecast_origin | Last observed session date | 2026-09-22 |
| horizon_sessions | Sessions ahead of origin | Integer, 1–70 |
| selected_model | Validation-selected forecasting model | Text model name |
| forecast_close | Model closing price estimate | USD; prediction, not observation |
| sim_lower_80 | Lower nominal eighty-percent envelope | USD; simulation 10th percentile |
| sim_upper_80 | Upper nominal eighty-percent envelope | USD; simulation 90th percentile |
| sim_lower_95 | Lower nominal ninety-five-percent envelope | USD; simulation 2.5th percentile |
| sim_upper_95 | Upper nominal ninety-five-percent envelope | USD; simulation 97.5th percentile |
| random_walk_close | Unchanged last-close baseline | USD |

Simulation envelopes are uncalibrated and omit model/parameter uncertainty. They are not guaranteed coverage intervals.

## Evaluation files

`validation_metrics.csv`: one row per model per validation fold. `test_metrics.csv`: one row per model on the single untouched test block. `selected_on_validation` marks the locked winner. `MAE_USD` and `RMSE_USD` are dollar errors; `NRMSE_origin_pct` = RMSE/origin close ×100; `MAPE_pct` and `sMAPE_pct` are percentage errors; `MASE` = MAE/mean training absolute one-session change; `R2` can be negative; `RMSE_skill_vs_random_walk` = 1−model RMSE/baseline RMSE; `origin_direction_accuracy_pct` measures direction relative to the forecast origin, not next-day trading accuracy.

`validation_predictions.csv` includes fold, model, horizon, actual, predicted and origin_price. `test_predictions.csv` contains date, actual_close and one predicted-price column per model. `alternative_model_forecasts.csv` contains future date and one forecast column per candidate. `evaluation_splits.csv` records split, train_rows, train_end, forecast_start, forecast_end and horizon. `model_leaderboard.csv` records mean/std validation origin-normalized RMSE and mean validation MAPE. `test_horizon_errors.csv` lists horizon-specific actual, forecast, absolute_error and APE_pct. All prices/errors are USD unless the name specifies percent.
