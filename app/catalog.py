class SchemaCatalog:
 def __init__(self,db): self.db=db
 def tables(self): return [r[0] for r in self.db.execute("select table_name from information_schema.tables where table_schema='main'").fetchall()]
