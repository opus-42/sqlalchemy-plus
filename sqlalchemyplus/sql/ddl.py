from sqlalchemy.sql.ddl import _CreateDropBase


class CreateView(_CreateDropBase):

    __visit_name__ = "create_view"

    def __init__(
        self, element, on=None, bind=None
    ):
        super(CreateView, self).__init__(element, on=on, bind=bind)


class DropView(_CreateDropBase):
    __visit_name__ = "drop_view"

    def __init__(
        self, element, on=None, bind=None
    ):
        super(DropView, self).__init__(element, on=on, bind=bind)
