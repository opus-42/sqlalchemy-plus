"""Test View and Materialized View Creation and Drop Statment."""

from sqlalchemy import Table, Column, MetaData, String, Integer
import sqlalchemy.dialects.postgresql as postgresql

from sqlalchemyplus.sql.schema import View, MaterializedView
from sqlalchemyplus.sql.ddl import (
    CreateView, DropView, CreateMaterializedView, DropMaterializedView
)

metadata = MetaData()
column1 = Column('id', Integer, primary_key=True)
column2 = Column('value1', String)
table1 = Table(
    'mytable',
    metadata,
    column1,
    column2,
)


def test_create_drop_matview():
    """Test create view."""
    matview1 = MaterializedView(
        'mymatview',
        MetaData(schema='myschema'),
        table1.select()
    )
    create_matview = CreateMaterializedView(matview1)
    drop_matview = DropMaterializedView(matview1)

    # Create
    sql_statement = str(create_matview.compile(dialect=postgresql.dialect()))
    raw_sql = "CREATE MATERIALIZED VIEW myschema.mymatview AS (SELECT mytable.id, mytable.value1 \nFROM mytable)"  # noqa
    assert raw_sql == sql_statement

    # Drop
    sql_statement = str(drop_matview.compile(dialect=postgresql.dialect()))
    raw_sql = "DROP MATERIALIZED VIEW myschema.mymatview"  # noqa
    assert raw_sql == sql_statement


def test_create_drop_view():
    """Test create view."""
    view1 = View(
        'myview',
        MetaData(schema='myschema'),
        table1.select()
    )
    create = CreateView(view1)
    drop = DropView(view1)

    # Create
    sql_statement = str(create.compile(dialect=postgresql.dialect()))
    raw_sql = "CREATE VIEW myschema.myview AS (SELECT mytable.id, mytable.value1 \nFROM mytable)"  # noqa
    assert raw_sql == sql_statement

    # Drop
    sql_statement = str(drop.compile(dialect=postgresql.dialect()))
    raw_sql = "DROP VIEW myschema.myview"  # noqa
    assert raw_sql == sql_statement
