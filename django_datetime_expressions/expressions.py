from django.db.models.expressions import Func
from django.db.models.fields import DateTimeField, IntegerField


class RelativeFunc(Func):
    output_field = DateTimeField()
    function = 'CAST'
    template = "%(expressions)s + %(function)s('%(calc_number)i %(convert_type)s' as INTERVAL)"

    def __init__(
        self,
        expression,
        calc_number: int,
        convert_type: str,
        output_field=None,
    ):
        super().__init__(
            expression,
            calc_number=calc_number,
            convert_type=convert_type,
            output_field=output_field,
        )
        self.calc_number = calc_number
        self.convert_type = convert_type

    def as_mysql(self, compiler, connection, **extra_content):
        self.function = 'DATE_ADD'
        self.template = "%(function)s(%(expressions)s, INTERVAL %(calc_number)i %(convert_type)s) as INTERVAL"
        return super().as_mysql(compiler, connection, **extra_content)

    def as_sqlite(self, compiler, connection, **extra_context):
        self.function = 'DATETIME'
        self.template = "%(function)s('%(expressions)s', '%(calc_number)i %(convert_type)s') as INTERVAL"
        return super().as_sqlite(compiler, connection, **extra_context)


class RelativeDay(RelativeFunc):
    """Coerce an expression to a new field type."""

    def __init__(self, expression, calc_number):
        super(RelativeDay, self).__init__(
            expression, calc_number, convert_type='days'
        )


class RelativeWeek(RelativeFunc):
    """Coerce an expression to a new field type."""

    def __init__(self, expression, calc_number):
        super(RelativeWeek, self).__init__(
            expression, calc_number, convert_type='weeks'
        )


class RelativeMonth(RelativeFunc):
    """Coerce an expression to a new field type."""

    def __init__(self, expression, calc_number):
        super(RelativeMonth, self).__init__(
            expression, calc_number, convert_type='months'
        )


class RelativeYear(RelativeFunc):
    """Coerce an expression to a new field type."""

    def __init__(self, expression, calc_number):
        super(RelativeYear, self).__init__(
            expression, calc_number, convert_type='years'
        )


class RelativeHour(RelativeFunc):
    """Coerce an expression to a new field type."""

    def __init__(self, expression, calc_number):
        super(RelativeHour, self).__init__(
            expression, calc_number, convert_type='hours'
        )


class RelativeMinute(RelativeFunc):
    """Coerce an expression to a new field type."""

    def __init__(self, expression, calc_number):
        super(RelativeMinute, self).__init__(
            expression, calc_number, convert_type='minutes'
        )


class RelativeSecond(RelativeFunc):
    """Coerce an expression to a new field type."""

    def __init__(self, expression, calc_number):
        super(RelativeSecond, self).__init__(
            expression, calc_number, convert_type='seconds'
        )


class Epoch(Func):
    template = 'EXTRACT(epoch FROM %(expressions)s)::INTEGER'
    output_field = IntegerField()
