"""A compilation for PostgreSQL."""
from sqlalchemy.ext.compiler import compiles

from sqlalchemyplus.sql.ddl import (
    CreateView, DropView, CreateMaterializedView, DropMaterializedView
)
from sqlalchemyplus.sql.schema import View, MaterializedView


# VIEW
@compiles(View, 'postgresql')
def visit_view(element, compiler, **kw):
    """Visit view statment."""
    return "{0}".format(element.fullname)


@compiles(CreateView, 'postgresql')
def visit_create_view(element, compiler, **kw):
    """Create View Compilation for PostgreSQL."""
    return "CREATE VIEW {0} AS ({1})".format(
        element.view.fullname,
        compiler.sql_compiler.process(element.view.as_select)
    )


@compiles(DropView, 'postgresql')
def visit_drop_view(element, compiler, **kw):
    """Create View Compilation for PostgreSQL."""
    statment = "DROP VIEW {0}".format(
        element.view.fullname,
    )
    if element.cascade:
        statment += "CASCADE"
    return statment


# MATERIALIZED VIEW
@compiles(MaterializedView, 'postgresql')
def visit_materialized_view(element, compiler, **kw):
    """Visit view statment."""
    return "{0}".format(element.fullname)


@compiles(CreateMaterializedView, 'postgresql')
def visit_create_materialized_view(element, compiler, **kw):
    """Create View Compilation for PostgreSQL."""
    return "CREATE MATERIALIZED VIEW {0} AS ({1})".format(
        element.element.fullname,
        compiler.sql_compiler.process(element.element.as_select)
    )


@compiles(DropMaterializedView, 'postgresql')
def visit_drop_materialized_view(element, compiler, **kw):
    """Create View Compilation for PostgreSQL."""
    statment = "DROP MATERIALIZED VIEW {0}".format(
        element.view.fullname,
    )
    if element.cascade:
        statment += "CASCADE"
    return statment
