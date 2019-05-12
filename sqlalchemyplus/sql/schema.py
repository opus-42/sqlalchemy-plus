"""A base for View and Materialized View definition.

To Dos :
 * Better instanciation of columns : remove the primary_key form the selected
 table, add row sql definition and column parsing from it, column from select
 with alias shoudl maybe be handled differently.
 * Add (unique) indexes for Materialized Views if passed as kwargs

"""

from sqlalchemy.sql.base import DialectKWArgs, _bind_or_error
from sqlalchemy.sql.selectable import FromClause, Immutable, Select
from sqlalchemy.sql.schema import SchemaItem, BLANK_SCHEMA, quoted_name


class ViewClause(DialectKWArgs, FromClause, Immutable, SchemaItem):
    """Represent a basic View representation."""

    named_with_column = True
    implicit_returning = False

    def __init__(self, name, metadata, as_select, **kwargs):
        """Instantiate a new View Clause."""
        super(ViewClause, self).__init__()
        if not isinstance(as_select, Select):
            self.as_select = as_select
            self._columns = None
        else:
            self.as_select = as_select
            self._columns = as_select.columns

        self.metadata = metadata
        self.bind = metadata.bind
        self.name = name

        self.schema = kwargs.pop("schema", None)
        if self.schema is None:
            self.schema = metadata.schema
        elif self.schema is BLANK_SCHEMA:
            self.schema = None
        else:
            quote_schema = kwargs.pop("quote_schema", None)
            self.schema = quoted_name(self.schema, quote_schema)

        self.indexes = set()
        self.constraints = set()
        self.foreign_keys = set()
        self.primary_keys = set()
        if self.schema is not None:
            self.fullname = "%s.%s" % (self.schema, self.name)
        else:
            self.fullname = self.name

    @property
    def _from_objects(self):
        return [self]

    def exists(self, bind=None):
        """Return True if this table exists."""
        if bind is None:
            bind = _bind_or_error(self)

        return bind.run_callable(
            bind.dialect.has_table, self.name, schema=self.schema
        )


class View(ViewClause):
    """A View Representation."""

    __visit_name__ = "view"

    def __init__(self,
                 name,
                 metadata,
                 as_select,
                 **kwargs):
        """Instantiate a view."""
        super().__init__(name, metadata, as_select)


class MaterializedView(ViewClause):
    """A Materialized View representation."""

    __visit_name__ = "materialized_view"

    def __init__(self,
                 name,
                 metadata,
                 as_select,
                 **kwargs):
        """Instantiate a Materialized View."""
        super().__init__(name, metadata, as_select)
