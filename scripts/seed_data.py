from pathlib import Path
from app.db import connect
Path('data').mkdir(exist_ok=True)
db=connect(); db.execute('drop table if exists sales'); db.execute('create table sales(order_id integer,product varchar,region varchar,revenue double)'); db.execute("insert into sales values (1,'AI Platform','South',1200),(2,'AI Platform','North',980),(3,'Data API','South',850),(4,'Data API','North',790),(5,'Voice Agent','South',1500),(6,'Voice Agent','West',1420),(7,'AgentOps','North',620),(8,'AgentOps','West',710)")
