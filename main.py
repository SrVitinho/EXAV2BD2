from neo4j import GraphDatabase
from DB import Database
from FamilySearches import FamilySearches
# Configuração da conexão com o Neo4j
db=Database("bolt://34.205.69.38:7687", "neo4j", "sediments-gate-gunfire")


Searches=FamilySearches(db)

Estudantes = Searches.get_estudantes()
print(Estudantes)

pais = Searches.get_pais("Vitor")
print(pais)

tios = Searches.get_tios("Julia")
print(tios)

irmao = Searches.get_irmao("Lisandra")
print(irmao)

dono = Searches.get_dono("Jotaro Matias")
print(dono)

db.close()