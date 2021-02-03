import pyspark

text_file = pyspark.SparkContext().textFile('pap.txt') 

counts = text_file.flatMap(lambda line : line.split(" "))
counts.saveAsTextFile('counts-words')

counts = counts.map(lambda word : (word, 1))
counts.saveAsTextFile('counts-mapped')

counts = counts.reduceByKey(lambda a, b : a + b)

counts.saveAsTextFile('counts-reduced')
