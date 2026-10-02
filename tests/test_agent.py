from app.agent import AnalyticsAgent
from app.db import connect
def test_top():
 d=connect(':memory:');d.execute('create table sales(product varchar,region varchar,revenue double)');d.execute("insert into sales values ('A','S',10),('A','N',20),('B','S',50),('C','S',30)");assert AnalyticsAgent(d).analyze('top products by revenue')['rows'][0]['product']=='B'
def test_total():
 d=connect(':memory:');d.execute('create table sales(product varchar,region varchar,revenue double)');d.execute("insert into sales values ('A','S',10),('B','N',20)");assert AnalyticsAgent(d).analyze('total revenue')['rows'][0]['total_revenue']==30.0
