from sqlalchemy.sql.base import DialectKWArgs
from sqlalchemy.sql.selectable import FromClause, Immutable, Select
from sqlalchemy.sql.schema import SchemaItem, BLANK_SCHEMA, quoted_name


class ViewClause(DialectKWArgs, FromClause, Immutable, SchemaItem):
    """Represent a base View"""

    __visit_name__ = "view"

    # def __new__(cls, *args, **kw):
    # TO DO here:
    # * Add construct that allow for various select_arguments
    # * Add an _add_table to the MetaData to  register the view

    def __init__(self, name, metadata, as_select, **kwargs):
        if not isinstance(as_select, Select):
            raise TypeError("as_select must be a Select statement")
        self.as_select = as_select
        self._columns = as_select.columns

        self.metadata = metadata
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
        if self.schema is not None:
            self.fullname = "%s.%s" % (self.schema, self.name)
        else:
            self.fullname = self.name
