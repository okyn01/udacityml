import pandas as pd
import matplotlib.pyplot as plt


def formatNum(num):
	return "{:.8f}".format(num)

def createdf(symbol):
	df = pd.read_json('data\\Binance_{}_1d_1 Jan, 2017-31 Mar, 2019.json'.format(symbol))
	df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'timeClose', 'QAS', 'NoT', 'TBA', 'TBQ', 'ignore']
	del df['QAS'], df['NoT'], df['TBA'], df['TBQ'], df['ignore'], df['timeClose']
	df['Date'] = pd.to_datetime(df['Date'],unit='ms')
	df.set_index('Date', inplace=True)
	return df



# LESSON 8
def lesson08():
	df = createdf('BNBBTC')
	print(df.tail(5))
	print(df.head(5))

# LESSON 9
def lesson09():
	df = createdf('BNBBTC')
	print(df[10:21]) #rows between 10 and 20

# LESSON 10
def get_max_close(symbol):
	df = createdf(symbol)
	return df['Close'].max()

# LESSON 11
def get_mean_close(symbol):
	df = createdf(symbol)
	return df['Close'].mean()

def lesson10_11():
	for symbol in ['BNBBTC', 'OMGBTC', 'NEOBTC', 'LTCBTC', 'XVGBTC']:
		print('Max close', symbol, formatNum(get_max_close(symbol)))
		print('Mean', symbol, formatNum(get_mean_close(symbol)))

# LESSON 12
def lesson12():
	df = createdf('LTCBTC')
	df['Close'].plot()
	plt.show()

# LESSON 14
def lesson14():
	df = createdf('LTCBTC')
	df[['Open', 'Close']].plot()
	plt.show()

lesson14()