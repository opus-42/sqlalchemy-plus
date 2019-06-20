"""Test select statment from views.

TO DOs:
- Use a better assert to compare SQL, i.e. we want to compare statment content
so not important if there are line breaks
"""

from sqlalchemy import Table, Column, MetaData, String, Integer
import sqlalchemy.dialects.postgresql as postgresql

from sqlalchemyplus.sql.schema import View

metadata = MetaData()
column1 = Column('id', Integer, primary_key=True)
column2 = Column('value1', String)
table1 = Table(
    'mytable',
    metadata,
    column1,
    column2,
)
view1 = View(
    'myview',
    MetaData(schema='myschema'),
    table1.select()
)


def test_select():
    """Select from a view clause."""
    select = view1.select()
    sql_statement = str(select.compile(dialect=postgresql.dialect()))
    raw_sql = "SELECT myschema.myview.id, myschema.myview.value1 \nFROM myschema.myview"  # noqa

    assert raw_sql == sql_statement
