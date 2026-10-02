import re
FORBIDDEN=re.compile(r'\b(INSERT|UPDATE|DELETE|DROP|ALTER|CREATE|COPY|ATTACH|DETACH|INSTALL|LOAD|CALL)\b',re.I)
def validate_read_only(sql):
 s=sql.strip().rstrip(';')
 if not s.lower().startswith(('select','with')): raise ValueError('Only SELECT/WITH queries are allowed')
 if FORBIDDEN.search(s) or ';' in s: raise ValueError('Only one read-only SQL statement is allowed')
