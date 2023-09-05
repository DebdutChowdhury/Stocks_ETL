import time
import datetime
import pandas as pd

ticker = ['AAPL','RELIANCE.NS','TATAMOTORS.BO','TATAMTRDVR.BO']
period1 = int(time.mktime(datetime.datetime(2023, 4, 1, 23, 59).timetuple()))
today = datetime.date.today()
period2 = int(time.mktime(today.timetuple()))
# int(time.mktime(datetime.datetime(2020, 12, 31, 23, 59).timetuple()))
interval = '1d' # 1d, 1m

# query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

# destination_file_path = "C:\\Users\\DEBDUT CHOWDHURY\\Desktop\\SSIS_Projects\\Stocks_ETL\\AAPL.csv"
# df = pd.read_csv(query_string)
# df.to_csv(destination_file_path,index=False)

for i in ticker:
    query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{i}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

    destination_file_path = f"C:\\Users\\DEBDUT\\Desktop\\SSIS_Projects\\Stocks_ETL\\Stocks\\{i}.csv"
    df = pd.read_csv(query_string)
    df.to_csv(destination_file_path,index=False)

