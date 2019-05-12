"""Test Views and Materialized View Definition."""
import pytest
from sqlalchemy import Table, Column, MetaData, String, Integer, select
from sqlalchemy.exc import UnboundExecutionError

from sqlalchemyplus.sql.schema import ViewClause

metadata = MetaData()
column1 = Column('id', Integer, primary_key=True)
column2 = Column('value1', String)
table1 = Table(
    'mytable',
    metadata,
    column1,
    column2,
)
# Note that most test are done on ViewClause since this parent class
# as the basic properties


def test_view_name():
    """Test view schema name and name assignment."""
    view_clause1 = ViewClause(
        'myview',
        MetaData(schema='myschema'),
        select('*')
    )
    assert view_clause1.fullname == 'myschema.myview'
    assert view_clause1.name == 'myview'

    view_clause2 = ViewClause(
        'myview',
        MetaData(schema='myschema'),
        select('*'),
        schema="myschema2"
    )
    assert view_clause2.fullname == 'myschema2.myview'
    assert view_clause2.name == 'myview'


def test_view_column():
    """Test View Column Assignment."""
    view_clause = ViewClause(
        'myview',
        MetaData(schema='myschema'),
        table1.select()
    )

    assert view_clause.c['id'].name == table1.c['id'].name
    assert view_clause.c['id'].type == table1.c['id'].type
    assert view_clause.c['value1'].name == table1.c['value1'].name
    assert view_clause.c['value1'].type == table1.c['value1'].type


def test_exists():
    """Test view or materialized view exists."""
    view_clause = ViewClause(
        'myview',
        MetaData(schema='myschema'),
        table1.select()
    )
    with pytest.raises(UnboundExecutionError):
        view_clause.exists()
