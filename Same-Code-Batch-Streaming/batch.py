from pyspark import SparkContext

sc = SparkContext("local[2]", "PubCount")

lines = sc.textFile("/vagrant/job/query_log.txt.2015-10-19-00.log")

pairs = lines.map(lambda line: (line.split("|")[3], 1))
pubCounts = pairs.reduceByKey(lambda x, y: x + y).sortBy(lambda x: x[1], ascending=False)

for (count, pub) in pubCounts.collect():
	print "{} : {}".format(pub, count)