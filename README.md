# Extending MapReduce with Apache Spark

No low-level, no under the hood stuff. Only high-level stuff.

## What is MapReduce?

1. Mapping your data set into <key, value> pairs
2. Then reducing over all pairs with the same key
3. In a distributed manner

In layman's terms:
- How to get frequencies of each word occurred in a 1000-page book?
- Tally marks (https://github.com/hisplan/Extending-MapReduce-with-Apache-Spark/blob/master/images/diagram-word-tally.png)
- Think of it as a divide-and-conquer strategy

## Hello, World / WordCount

Process Diagram:
https://github.com/hisplan/Extending-MapReduce-with-Apache-Spark/blob/master/images/diagram-mapreduce-wordcount-process.png

e.g. Counting Clicks (Anomaly Detection project):

Raw
```
Jun 20|bloomberg|5|...
Jun 20|forbes|5|...
Jun 21|bloomberg|5|...
Jun 21|synacor|3|...
Jun 22|synacor|7|...
Jun 23|bloomberg|5|...
```

Mapped
```
(bloomberg, 10)
(forbes, 5)
(bloomberg, 15)
(synacor, 3)
(synacor, 7)
(bloomberg, 5)
```

Reduced
```
(bloomberg, 30)
(forbes, 5)
(synacor, 10)
```

## Frameworks

- Google MR
- Apache Hadoop
- Apache Spark
- ...

## Extending How?

### Really Fast

- In-memory (vs. disk)
- Sort 1 PB of data (10 trillion records)
 - Spark : under 4 hours on 190 machines (public cloud; AWS)
 - Hadoop : 16 hours on 3,800 machines (dedicated data center)
 - https://databricks.com/blog/2014/10/10/spark-petabyte-sort.html

### Easy to Use

- On laptop
- High-level APIs, not much of boilerplate required
 - 50 lines Hadoop vs. 3 lines Spark
 - https://github.com/hisplan/Extending-MapReduce-with-Apache-Spark/tree/master/wordcount-spark-vs-hadoop
 
Apply functions to results of SQL

```
results = context.sql( "SELECT * FROM people" )
names = results.map(lambda p: p.name)
```

SQL against CSV, JSON, ...

```
context.jsonFile("s3n://...").registerTempTable("json")
results = context.sql( "SELECT * FROM people JOIN json ..." )
```

- Java, Scala, Python, R, SQL
- Same code, same system for batch and streaming
 - https://github.com/hisplan/Extending-MapReduce-with-Apache-Spark/tree/master/same-code-batch-and-streaming

### Multiple Types of Computations

There are all built-in:

- Batch
- Streaming
- SQL and DataFrames
- MLlib (machine learning)
- GraphX (parallel graph computations)

### Interactivity

- Built-in REPL (Read, Eval, Print, Loop)
- Multiple implementations of iPython-like Notebook

### Cluster

- Standalone cluster (no YARN or MESOS required)
- AWS
- Databricks
- My own Raspberry PI cluster!

## DEMO

### Zeppelin

- Batch: Query Log
- Streaming: Twitter (Sentiment, Coverage, Trend Analysis)

### Databricks

- Creating my own cluster
- Batch: Query Log / AWS
- Machine Learning: Spam Filter
