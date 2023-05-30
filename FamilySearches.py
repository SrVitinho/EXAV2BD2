class FamilySearches:
    def __init__(self, database):
        self.db = database

    def get_estudantes(self):
        query = "match (e:Estudante) return e.name AS nomes"
        results = self.db.execute_query(query)
        return [result["nomes"] for result in results]

    def get_pais(self, nome):
        query = f"match (p1:Pessoa)-[:pai_do]->(p2:Pessoa {{name: '{nome}'}}) return p1.name AS nome_pais"
        results = self.db.execute_query(query)
        return [result["nome_pais"] for result in results]

    def get_tios(self, nome_sobrinho):
        query = f"match (p1:Pessoa)-[:tio_do]->(p2:Pessoa {{name: '{nome_sobrinho}'}}) return p1.name AS nome_tios"
        results = self.db.execute_query(query)
        return [result["nome_tios"] for result in results]

    def get_irmao(self, nome_irmao):
        query = f"match (p1:Pessoa)-[:irmão_do]->(p2:Pessoa {{name: '{nome_irmao}'}}) return p1.name AS nome_irmaos"
        results = self.db.execute_query(query)
        return [result["nome_irmaos"] for result in results]

    def get_dono(self, nome_pet):
        query = f"match (p1:Pessoa)-[:dono_do]->(t:Pet {{name: '{nome_pet}'}}) return p1.name AS nome_dono"
        results = self.db.execute_query(query)
        return [result["nome_dono"] for result in results]