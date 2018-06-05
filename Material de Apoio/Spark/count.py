from pyspark import SparkContext

arquivo = "hdfs://dricardo-master:9000/user/engdados/texto.txt"

sc = SparkContext("local", "ContadorPalavras")

text_file = sc.textFile(arquivo)

counts = text_file.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

counts.saveAsTextFile("hdfs://dricardo-master:9000/user/engdados/resultado2")

print("Resultado: ")
print(counts.collect())
