import pandas as pd
import matplotlib.pyplot as plt


'''
252 trading days per year

'''


def formatNum(num):
	return "{:.8f}".format(num)

def createdf(symbol):
	df = pd.read_json('data\\Binance_{}_1d_1 Jan, 2017-31 Mar, 2019.json'.format(symbol))
	df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'timeClose', 'QAS', 'NoT', 'TBA', 'TBQ', 'ignore']
	del df['QAS'], df['NoT'], df['TBA'], df['TBQ'], df['ignore'], df['timeClose']
	df['Date'] = pd.to_datetime(df['Date'],unit='ms')
	df.set_index('Date', inplace=True)
	return df



def lesson08():
	start_date = '2018-01-22'
	end_date = '2018-01-26'
	dates = pd.date_range(start_date, end_date)
	df1 = pd.DataFrame(index=dates)
	print(df1)

def lesson09():
	start_date = '2018-01-22'
	end_date = '2018-01-26'
	dates = pd.date_range(start_date, end_date)
	df1 = pd.DataFrame(index=dates)

	dfBNB = createdf('BNBBTC')
