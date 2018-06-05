#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from pyspark import SparkContext
from pyspark.sql import SparkSession
from datetime import datetime

spark = SparkSession.builder.appName("Onibus").getOrCreate()

linhas_rdd = spark.read.json("hdfs://dricardo-master:9000/user/engdados/onibus/2018_04_21_linhas.json").rdd
tabelas_rdd = spark.read.json("hdfs://dricardo-master:9000/user/engdados/onibus/2018_04_21_tabelaLinha.json").rdd
trechos_rdd = spark.read.json("hdfs://dricardo-master:9000/user/engdados/onibus/2018_04_21_trechosItinerarios.json").rdd

# Codigo e nome da linha dos onibus

codigo_nome = linhas_rdd.map(lambda linha: (linha['COD'], linha['NOME']))

# Mapeia o codigo, ponto e horário.

#codigo_horarios = tabelas_rdd.map(lambda linha: (linha['COD'], (linha['PONTO'], int(linha['DIA']), linha['HORA'])))

codigo_horarios = tabelas_rdd.map(lambda linha: (linha['COD'], (linha['PONTO'], 
    datetime.strptime("{} {} {}".format("0", linha['DIA'], linha['HORA']), "%W %w %H:%M")
)))

# Faz o join entre as linhas, nomes e horários

#linhas_horarios = codigo_nome.join(codigo_horarios)

# Resultado (codigo, nome da linha e horarios)

horarios_agrupados = codigo_horarios.groupByKey().mapValues(list)

resultado = codigo_nome.join(horarios_agrupados)

#resultado.saveAsTextFile("hdfs://dricardo-master:9000/user/engdados/onibus/resultado")

# Exibe as linhas e os horários

#linhas = resultado.collect()
linhas = resultado.take(10)

for linha in linhas:
    print '* Linha {}: {}'.format(linha[0], linha[1][0])
    print '- Terminal e Horários: '
    for th in linha[1][1]:
        print '    {} - {}'.format(th[0], th[1].strftime('%A %H:%M'))
    print '------------------------------------------------------------'

