from pyspark.sql import SparkSession
import nltk
import re

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("WordCount") \
    .getOrCreate()

sc = spark.sparkContext

# Read all text files in the books_smaller directory
book_rdd = sc.wholeTextFiles("bookCorpus_small/*")

# Combine the content of all files into a single RDD
combined_rdd = book_rdd.map(lambda x: x[1])

# Data transformation - remove tabs and non-word characters
book_rdd = combined_rdd.flatMap(lambda x: re.sub(r'\t', '', x).split())
book_rdd = book_rdd.map(lambda x: re.sub(r'[^\w\s]', '', x))

# Word count calculation
book_count = book_rdd.map(lambda word: (word, 1))
book_wc = book_count.reduceByKey(lambda x, y: x + y)

# Save word count results
book_wc.saveAsTextFile('/user/hadoop/spark_wc_local')

# Stop SparkContext
sc.stop()
