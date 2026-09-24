# SNDK Stock Data: EDA & 2026 Forecast

**Title:** SNDK Stock Data: EDA & 2026 Forecast (36 characters)

**Subtitle:** Sandisk daily OHLCV, interactive EDA and time-series machine learning forecasts (79 characters)

**Author:** Muhammad Ibrahim Shahrukh

## Dataset description

Explore Sandisk (NASDAQ: SNDK) daily stock prices and trading volume with a clean, beginner-friendly dataset and a complete machine-learning notebook. This snapshot contains **403 daily observations from February 13, 2025 through September 22, 2026**, with seven plainly named columns: date, ticker, open, high, low, close and volume. Prices are reported in USD per share on the basis supplied in the original file; price-adjustment settings were not recorded.

The accompanying notebook walks through validation, candlestick and volume dashboards, return distributions, monthly performance, drawdowns, volatility, correlations, autocorrelation and stationarity diagnostics. It compares eight forecasting candidates: a random-walk baseline, recent log drift, Ridge regression, Random Forest, Extra Trees, histogram gradient boosting, XGBoost and CatBoost. Three chronological validation blocks select a model before a separate 70-session test. Forecasts extend from the snapshot cutoff through December 31, 2026, with simulated uncertainty envelopes and clearly separated historical and predicted data.

This resource is useful for learning pandas, Plotly, exploratory financial analysis and leakage-aware time-series evaluation. It is not live market data, a trading signal service or a guarantee of future prices. Raw quotes are structurally checked but not independently authenticated. Six observations preceding the February 24, 2025 regular listing remain in the historical CSV and are excluded from the main models. The short history and unknown adjustment basis limit interpretation.

## What is in this SNDK dataset?

A single stock's observed daily OHLCV history. The main CSV contains **only historical observations**; engineered indicators and future forecasts are separate files.

## What can I do with it?

Practice price/volume charts, return and volatility analysis, data validation, chronological model evaluation and uncertainty-aware forecasting. Do not treat correlations or model estimates as evidence of a profitable strategy.

## Main file description

`sndk_daily_clean.csv` contains 403 observed SNDK daily records from 2025-02-13 through 2026-09-22 in chronological order. Each row includes an ISO trading date, ticker, open/high/low/close prices in USD per share and integer share volume. The yfinance-style metadata rows have been removed, column names standardized and structural checks completed without filling missing sessions, discarding extreme moves or adding forecasts. All supplied observations are retained; adjustment status and original collection parameters are unknown.

## Column descriptions

| Column | Description (1–5 words) | Type | Unit / details |
|---|---|---|---|
| date | Trading session date | date | YYYY-MM-DD; exchange-local date label |
| ticker | Stock ticker symbol | text | SNDK |
| open | Session opening price | float | USD per share, as supplied |
| high | Session highest price | float | USD per share, as supplied |
| low | Session lowest price | float | USD per share, as supplied |
| close | Session closing price | float | USD per share, as supplied |
| volume | Shares traded | integer | Shares, nonnegative |

## Provenance and collection methodology

The uploader reports collecting this snapshot from **Yahoo Finance using yfinance**. The export has the recognizable Price/Ticker/Date header layout. The exact API call, original retrieval date, package version, price adjustment settings and session configuration were not supplied, so they are not inferred. Preparation on 2026-09-24 used the uploaded file; no replacement history was downloaded. See `PROVENANCE.md` for the original-file hash, transformations, collection example and source links.

## Suggested tags

Finance, Stock Market, Time Series, Exploratory Data Analysis, Machine Learning, Forecasting, Data Visualization, Sandisk, SNDK.

## Citation and rights

Shahrukh, Muhammad Ibrahim. *SNDK Stock Data: EDA & 2026 Forecast*. Prepared 2026-09-24 from a user-supplied Yahoo Finance/yfinance snapshot ending 2026-09-22. Source: https://finance.yahoo.com/quote/SNDK/history/; collection tool: https://ranaroussi.github.io/yfinance/.

**Data redistribution license is unverified.** Do not label these source prices CC0, public domain or otherwise openly licensed without an appropriate basis. yfinance's software license is separate from rights in Yahoo market data. Consult source terms before public redistribution.
