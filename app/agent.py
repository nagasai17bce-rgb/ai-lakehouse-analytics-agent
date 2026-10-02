import time
from .catalog import SchemaCatalog
from .executor import QueryExecutor
from .planner import RuleBasedPlanner
from .safety import validate_read_only
class AnalyticsAgent:
 def __init__(self,db): self.catalog=SchemaCatalog(db); self.planner=RuleBasedPlanner(); self.executor=QueryExecutor(db)
 def analyze(self,question):
  t=time.perf_counter(); p=self.planner.build(question); validate_read_only(p.sql); cols,rows=self.executor.execute(p.sql)
  return {'question':question,'intent':p.intent,'sql':p.sql,'columns':cols,'rows':rows,'row_count':len(rows),'latency_ms':round((time.perf_counter()-t)*1000,2),'tables_considered':self.catalog.tables()}
