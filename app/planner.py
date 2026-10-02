from dataclasses import dataclass
@dataclass(frozen=True)
class Plan: sql:str; intent:str
class RuleBasedPlanner:
 def build(self,q):
  x=q.lower()
  if 'top' in x and 'product' in x and 'revenue' in x:return Plan("select product,round(sum(revenue),2) revenue from sales group by product order by revenue desc limit 3",'top_products_by_revenue')
  if 'total' in x and 'revenue' in x:return Plan("select round(sum(revenue),2) total_revenue from sales",'total_revenue')
  if 'orders' in x and 'region' in x:return Plan("select region,count(*) orders from sales group by region order by orders desc",'orders_by_region')
  raise ValueError('No deterministic plan matched; add an LLM planner adapter.')
