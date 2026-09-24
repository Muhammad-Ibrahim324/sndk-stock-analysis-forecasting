# Provenance & transformation log

Author: Muhammad Ibrahim Shahrukh. Prepared: 2026-09-24.

## Chain of custody

- Input: user attachment `sndk_stock_data(1).csv`, copied byte-for-byte to `data/raw/sndk_yfinance_original.csv`.
- Uploader-reported upstream provider: Yahoo Finance; collection client: yfinance.
- Original SHA-256: `d64f838344743dff00005b12b4ecced9328ae6f46840ea0d624ba61a833a2a23`.
- Original retrieval timestamp, yfinance version, request arguments and adjustment flags: **not provided**.
- Observed range: 2025-02-13 to 2026-09-22; 403 observations. No live price download occurred during preparation.
- The date of this document is a preparation date, not the source acquisition date.
- Yahoo's SNDK historical page was not accessible through the research tool, so no independent row-level quote reconciliation is claimed.

## Transformations, in order

1. Read the first CSV row as field names. Verify ticker metadata says SNDK.
2. Remove the second (`Ticker`) and third (`Date`) metadata rows, not price observations.
3. Rename `Price` to `date`; lowercase price/volume field names; add constant ticker SNDK.
4. Parse dates, numeric prices and integer volumes; sort date ascending.
5. Reorder as date, ticker, open, high, low, close, volume.
6. Assert date uniqueness, no missing cells, numeric finiteness, positive prices, nonnegative integer volume and consistent OHLC bounds.
7. Verify expected sessions against a documented calendar. Do not insert fabricated prices for market closures.
8. Serialize clean CSV with an ISO date and without a pandas index. Do not round quotes to cents, fill data, winsorize returns or apply corporate-action adjustments.

All 403 rows survive. Parsing and serializing IEEE floating-point values can change textual representation at machine precision; the raw file preserves exact original bytes. Six rows preceding regular listing are retained and flagged in the analysis features. Main forecasting uses the 397 rows beginning 2025-02-24. No `Adj Close` column or corporate-action table is supplied; the basis of OHLC prices cannot be established from the CSV alone.

## Derived fields

Daily percentage return: `100*(close/previous_close-1)`; log return: `log(close/previous_close)`; intraday range: `100*(high-low)/open`; overnight gap: `100*(open/previous_close-1)`; SMA: trailing close mean; annualized volatility: trailing 20-session sample standard deviation of log returns × √252 ×100; drawdown: `100*(close/running_max_close-1)`; volume ratio: current volume divided by trailing 20-session mean. All windows include only current/past observations. Initial unavailable values remain blank in the features file.

Model training targets the next log return. Forecast inputs contain five recent returns, trailing means/stds over 5/10/21 sessions and sums over 5/21 sessions. All transformations are fitted within each training fold. Future inputs are generated recursively from predicted returns, never future observed prices/volume. See the notebook for full formulas, fixed model configurations and fold dates.

## Example for collecting a new snapshot

This is a documented new workflow, **not a claim about the original collection call**:

```python
import datetime, json, yfinance as yf
args = dict(tickers='SNDK', start='2025-02-13', end='2026-09-23',
            interval='1d', auto_adjust=False, actions=True, repair=False, prepost=False)
data = yf.download(**args)
data.to_csv('sndk_fresh_unadjusted_with_actions.csv')
metadata = dict(retrieved_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                yfinance_version=yf.__version__, parameters=args)
with open('collection_metadata.json','w') as f:
    json.dump(metadata,f,indent=2)
```

The end date is exclusive. Retain dividends and splits, state whether analysis uses adjusted or unadjusted prices, and version each download because historical data may be revised. This optional snippet is not executed by the notebook and yfinance is not required for snapshot analysis.

## Sources consulted

- Yahoo Finance SNDK history: https://finance.yahoo.com/quote/SNDK/history/ (uploader-identified data source).
- yfinance documentation and data-use notice: https://ranaroussi.github.io/yfinance/.
- yfinance download parameters: https://ranaroussi.github.io/yfinance/reference/api/yfinance.download.html.
- Sandisk listing announcement: https://investor.sandisk.com/news-releases/news-release-details/sandisk-celebrates-nasdaq-listing-after-completing-separation.
- Nasdaq 2026 holidays/early closes: https://www.nasdaq.com/market-activity/stock-market-holiday-schedule.
- NYSE calendar: https://www.nyse.com/markets/hours-calendars.
- Chronological evaluation reference: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html.

## Reuse rights

No open-data redistribution license has been verified. yfinance is unofficial and its documentation directs users to Yahoo's data-use terms. A software license does not license the downloaded prices. Confirm permission before redistributing source data or applying a Kaggle data license. No blanket license has been added to this repository.
