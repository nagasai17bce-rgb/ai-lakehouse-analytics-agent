import pytest
from app.safety import validate_read_only
@pytest.mark.parametrize('sql',['DELETE FROM sales','DROP TABLE sales','UPDATE sales SET revenue=0','SELECT 1; DROP TABLE sales'])
def test_block(sql):
 with pytest.raises(ValueError):validate_read_only(sql)
def test_allow():validate_read_only('select * from sales')
