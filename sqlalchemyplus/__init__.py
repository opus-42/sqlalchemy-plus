__version__ = "0.1.0"

import sqlalchemyplus.compiled.postgresql as postgresql  # noqa

from sqlalchemyplus.sql.schema import View, MaterializedView  # noqa
from sqlalchemyplus.sql.ddl import (  # noqa
    CreateView, CreateMaterializedView, DropView, DropMaterializedView)  # noqa
