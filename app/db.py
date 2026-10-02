import duckdb

def connect(path='data/analytics.duckdb'): return duckdb.connect(path)
