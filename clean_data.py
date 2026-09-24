"""Rebuild the beginner-friendly CSV without downloading or adjusting prices."""
from pathlib import Path
import csv
import pandas as pd
import numpy as np

root = Path(__file__).resolve().parent
source = root / 'data/raw/sndk_yfinance_original.csv'
with source.open(newline='') as f:
    rows = csv.reader(f)
    fields, tickers, date_header = next(rows), next(rows), next(rows)
assert fields == ['Price','Close','High','Low','Open','Volume']
assert tickers == ['Ticker'] + ['SNDK']*5
assert date_header[0] == 'Date'
df = pd.read_csv(source,skiprows=[1,2]).rename(columns={'Price':'date'})
df.columns = df.columns.str.lower()
df['date'] = pd.to_datetime(df['date'],errors='raise')
for col in ['open','high','low','close','volume']:
    df[col] = pd.to_numeric(df[col],errors='raise')
df.insert(1,'ticker','SNDK')
df = df[['date','ticker','open','high','low','close','volume']].sort_values('date').reset_index(drop=True)
assert df.date.is_unique and not df.isna().any().any()
assert np.isfinite(df[['open','high','low','close','volume']]).all().all()
assert (df[['open','high','low','close']]>0).all().all()
assert (df.volume>=0).all() and (df.volume%1==0).all()
assert (df.high>=df[['open','close','low']].max(axis=1)).all()
assert (df.low<=df[['open','close','high']].min(axis=1)).all()
df['volume'] = df.volume.astype('int64')
destination = root/'data/sndk_daily_clean.csv'
df.to_csv(destination,index=False,date_format='%Y-%m-%d')
print(f'Saved {len(df)} observations to {destination}')
