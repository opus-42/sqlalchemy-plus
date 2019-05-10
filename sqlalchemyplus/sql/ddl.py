"""Additionnal DDL for SQL Alchemy."""

from sqlalchemy.sql.ddl import _CreateDropBase


class _CreateDropBaseView(_CreateDropBase):
    """A base for Create and Drop View."""

    def __init__(self, element, cascade=False, on=None, bind=None):
        self.view = element
        self.cascade = cascade
        super().__init__(element, on=on, bind=bind)


class CreateView(_CreateDropBaseView):
    """Represent a CREATE VIEW statment."""

    __visit_name__ = "create_view"

    def __init__(self, element, on=None, bind=None):
        """Create a new CREATE VIEW statment."""
        super().__init__(element, on=on, bind=bind)


class DropView(_CreateDropBaseView):
    """Represent a DROP VIEW statment."""

    __visit_name__ = "drop_view"

    def __init__(self, element, cascade=False, on=None, bind=None):
        """Create a new DROP VIEW statment."""
        super().__init__(element, cascade=cascade, on=on, bind=bind)


class CreateMaterializedView(_CreateDropBaseView):
    """Represent a CREATE MATERIALIZED VIEW statment."""

    __visit_name__ = "create_view"

    def __init__(self, element, on=None, bind=None):
        """Create a new CREATE MATERIALIZED VIEW statment."""
        super().__init__(element, on=on, bind=bind)


class DropMaterializedView(_CreateDropBaseView):
    """Represent a DROP MATERIALIZED VIEW statment."""

    __visit_name__ = "drop_view"

    def __init__(self, element, cascade=False, on=None, bind=None):
        """Create a new DROP MATERIALIZED VIEW statment."""
        super().__init__(element, cascade=cascade, on=on, bind=bind)
