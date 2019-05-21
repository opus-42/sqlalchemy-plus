# SQL Alchemy Plus

This package provide additional package definition for SqlAlchemy
that are specific for PostgreSQL and other database.

Here are the currently supported features (database supported):
* View (PostgreSQL)
* Materialized View (PostgreSQL)


## Installation

Install SQL Alchemy Plus using pip

```bash
pip install sqlalchemyplus
```

## Quick start

**Define a View or a Materialized View programmatically**

```
from sqlalchemy import Table, select, Column, MetaData, Integer, String
from sqlalchemyplus import View

metadata = MetaData()
table = Table('mytable',
              metadata,
              Column('key', Integer),
              Column('value', String))

select_table = table.select()
view = View(
    'myview',
    metadata,
    select_table
)

```
