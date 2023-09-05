import yfinance as yfs
import pandas as pd

data = yfs.download("RELIANCE.NS")
data.to_csv("Reliance.csv")