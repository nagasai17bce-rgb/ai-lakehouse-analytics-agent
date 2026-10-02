class QueryExecutor:
 def __init__(self,db): self.db=db
 def execute(self,sql):
  c=self.db.execute(sql); cols=[d[0] for d in c.description]; return cols,[dict(zip(cols,r)) for r in c.fetchall()]
