#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymongo import MongoClient
client = MongoClient('localhost', 27017)

# Cria o banco de dados.

db = client.atividade1

# Cria a collection alunos.

alunos = db.alunos

# Abre o arquivo com os dados dos alunos.

with open('discentes.txt', 'r') as arq:
    linhas = arq.readlines()

atributos = linhas[0].replace('"', '').strip().split(";")

for i in range(1, len(linhas), 1):
    post = dict()
    dados = linhas[i].replace('"', '').strip().split(";")
    for i in range(len(atributos)):
        post[atributos[i]] = dados[i]
    alunos.insert_one(post)

client.close()
       







