from pyspark import SparkContext
from pyspark.streaming import StreamingContext

# create a local StreamingContext with two working thread and batch interval of 3 seconds
sc = SparkContext("local[2]", "NeworkPubCount")
ssc = StreamingContext(sc, 3)

# create a DStream that will connect to localhost:9999
pubs = ssc.socketTextStream("127.0.0.1", 9999)

pairs = lines.map(lambda line: (line.split("|")[3], 1))
pubCounts = pairs.reduceByKey(lambda x, y: x + y).transform(lambda rdd: rdd.sortBy(lambda x:x[1], ascending=False))

# print the first five elements of each RDD generated in this DStream to the console
pubCounts.pprint(num=5)

ssc.start()             # Start the computation
ssc.awaitTermination()  # Wait for the computation to terminate
