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
	'''
	Create a dataframe with a start and end index date
	'''
	start_date = '2018-01-22'
	end_date = '2018-01-26'
	dates = pd.date_range(start_date, end_date)
	df1 = pd.DataFrame(index=dates)
	print(df1)

def lesson09():
	'''
	Create a dataframe with a start and end index date
	Then do a join (by default left) so only the start and end date will be joined from the other dataframe
	Make sure that the dataframe you want to join has same index
	'''
	start_date = '2018-01-22'
	end_date = '2018-01-26'
	dates = pd.date_range(start_date, end_date)
	df1 = pd.DataFrame(index=dates)

	dfBNB = createdf('BNBBTC')

	df1=df1.join(dfBNB, how='left') # default is left, also have right, inner and outer
	df1 = df1.dropna() # Drop all NaN, not a number values
	print(df1)


def lesson11():
	'''
	Join multiple stocks in one dataframe
	'''
	start_date = '2018-01-22'
	end_date = '2018-01-26'
	dates = pd.date_range(start_date, end_date)
	df1 = pd.DataFrame(index=dates)

	dfBNB = createdf('BNBBTC')

	df1=df1.join(dfBNB, how='left') # default is left, also have right, inner and outer
	df1 = df1.dropna() # Drop all NaN, not a number values

	symbols = ['OMGBTC']

	for symbol in symbols:
		df_temp = createdf(symbol)
		df_temp = df_temp['Close'] # make dataframe as one column with close
		df_temp.columns = [ 'symbol'] # rename column so it doesn't have the same name (all columns must have different names)
		#print(df_temp.head())
		df = df1.join(df_temp)


	print(df)

lesson11()

