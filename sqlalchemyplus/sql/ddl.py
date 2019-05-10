from sqlalchemy.sql.ddl import _CreateDropBase


class CreateView(_CreateDropBase):
    """Represent a CREATE VIEW statment."""

    __visit_name__ = "create_view"

    def __init__(self, element, on=None, bind=None):
        """Create a new CREATE VIEW statment."""
        super(CreateView, self).__init__(element, on=on, bind=bind)


class DropView(_CreateDropBase):
    """Represent a DROP VIEW statment."""

    __visit_name__ = "drop_view"

    def __init__(self, element, on=None, bind=None):
        """Create a new DROP VIEW statment."""
        super(DropView, self).__init__(element, on=on, bind=bind)


class CreateMaterializedView(_CreateDropBase):
    """Represent a CREATE MATERIALIZED VIEW statment."""

    __visit_name__ = "create_view"

    def __init__(self, element, on=None, bind=None):
        """Create a new CREATE MATERIALIZED VIEW statment."""
        super(CreateView, self).__init__(element, on=on, bind=bind)


class DropMaterializedView(_CreateDropBase):
    """Represent a DROP MATERIALIZED VIEW statment."""

    __visit_name__ = "drop_view"

    def __init__(self, element, on=None, bind=None):
        """Create a new DROP MATERIALIZED VIEW statment."""
        super(DropView, self).__init__(element, on=on, bind=bind)
