from pyspark import SparkContext	

sc = SparkContext('local', 'Tweet Spark')

data = sc.textFile('2352345')
data = data.filter(lambda row: row != '')
tweet_recs = data.map(lambda row: row.split(','))
tweets = tweet_recs.map(lambda cols: cols[0], cols[3)
