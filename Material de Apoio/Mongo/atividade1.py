#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymongo import MongoClient
client = MongoClient('localhost', 27017)

# Cria o banco de dados.

db = client.atividade1

# Cria a collection alunos.

alunos = db.alunos

res = alunos.find({"nome_curso": {"$in": ["ENGENHARIA DE COMPUTAÇÃO", "TECNOLOGIA DA INFORMAÇÃO", "CIÊNCIA DA COMPUTAÇÃO", "CIÊNCIAS E TECNOLOGIA"] } } )
print(list(res))

exit()
# Teste com operadores

res = alunos.find({"nivel_ensino": {"$in": ["TECNOLOGIA DA INFORMAÇÃO", "DOUTORADO",]}})

# Busca alunos que ingressaram por vestibular.

#res = alunos.find({"forma_ingresso": "VESTIBULAR"})
#for a in res:
#    print(a['nome_discente'])
#exit()

alunos_vestibular = list(alunos.find({"forma_ingresso": "VESTIBULAR"}).sort("nome_discente"))

print("\n---------- ALUNOS QUE INGRESSARAM POR VESTIBULAR ----------\n")
for aluno in alunos_vestibular:
    print("{} - {}".format(aluno['nome_discente'], aluno['matricula']))

# Busca alunos que ingressaram no mestrado.

alunos_mestrado = list(alunos.find({"sigla_nivel_ensino": "E"}))

print("\n---------- ALUNOS QUE INGRESSARAM NO MESTRADO ----------\n")
for aluno in alunos_mestrado:
    print("{} - {}".format(aluno['nome_discente'], aluno['matricula']))

# Busca alunos de uma unidade gestora específica.

unidade_gestora = "CENTRO DE TECNOLOGIA"
alunos_unidade_gestora = list(alunos.find({"nome_unidade": unidade_gestora}))


print("\n---------- ALUNOS DA UNIDADE {} ----------\n".format(unidade_gestora))
for aluno in alunos_unidade_gestora:
    print("{} - {}".format(aluno['nome_discente'], aluno['matricula']))

client.close()

