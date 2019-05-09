"""Definition of SQL Syntax used to compile every statment.

SQL base syntaxic elements such as CREATE or DROP are defined here.
They are handle in each SQLStatment. SQLStatment represents the base
abstraction for each SQL statement
and define it as a list of syntaxic elements.

Todo:
    * Add more option to SQLSyntaxElement Compilation
    * Provide a example section in the docstrings
"""


def item_action(item):  # noqa
    """Returns actionnable method for the specified item.

    Args:
        item (any): Any object with a compile method.

    Returns:
        function: An actionnable method.

    """

    def action(self, element=None):
        """Perform an action."""
        self.append(item.compile(element))
        return self
    return action


class SQLSyntaxElement(object):
    """A representation of an SQL Syntaxic Element such as CREATE.

    Args:
        value (string): plain syntax of the element ex: 'CREATE' .

    Attributes:
        value

    """

    def __init__(self, value):
        """Instantiate a new SQLSyntaxElement."""
        self.value = value.upper()

    def compile(self, element=None):
        """Compile the Syntax Element into plain string.

        Args:
            element (str): Additionnal parameter linked to the elementself.
                           It may be the name of a 'TABLE' or a 'VIEW'

        Returns:
            type: Description of returned object.

        """
        if element:
            return ' '.join([self.value, element])
        else:
            return self.value


class SQLStatment(object):
    """A base abstraction for any SQL Statment.

    Attributes:
        items (list): A list of SQL Syntaxic Items.

    """

    SQL_MAPPING = {
        '_or': SQLSyntaxElement('OR'),
        '_as': SQLSyntaxElement('AS'),
        'create': SQLSyntaxElement('CREATE'),
        'drop': SQLSyntaxElement('DROP'),
        'temporary': SQLSyntaxElement('TEMPORARY'),
        'view': SQLSyntaxElement('VIEW'),
    }

    def __new__(cls, *args, **kw):
        """Create a new SQLStatment."""
        for key, item in cls.SQL_MAPPING.items():
            setattr(cls, key, item_action(item))

        return super().__new__(cls)

    def __init__(self):
        """Instantiate a new SQLStatment."""
        self.items = []

    def append(self, sql_clause):
        """Add a new SQL syntaxic element to the current statment.

        Args:
            sql_clause (SQLSyntaxElement): a string or an SQLSyntaxElement

        """
        if not sql_clause:
            pass
        elif isinstance(sql_clause, SQLSyntaxElement):
            self.items.append(sql_clause.compile())
        else:
            self.items.append(sql_clause)

    @property
    def compiled(self):
        """Get the properly defined SQL statment."""
        return ' '.join(self.items)
