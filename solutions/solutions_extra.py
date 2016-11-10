# Solution to extra credit exercise:
series = ['JTSJOL', 'JTSQUL', 'JTSHIL', 'JTSLDL']
names = ['openings', 'quits', 'hires', 'layoffs']
from pandas_datareader.data import DataReader

res = DataReader(series, start='2000-01-01', data_source="fred")

res = res.rename(columns=dict(zip(series, names)))

ax = res[['quits', 'layoffs']].plot.area()
res[['hires', 'openings']].plot(ax=ax)
