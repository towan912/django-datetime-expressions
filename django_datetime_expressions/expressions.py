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


class RelativeDay(RelativeFunc):
    """Coerce an expression to a new field type."""

    def __init__(self, expression, calc_number):
        super(RelativeDay, self).__init__(
            expression, calc_number, convert_type='day'
        )


class RelativeWeek(RelativeFunc):
    """Coerce an expression to a new field type."""

    def __init__(self, expression, calc_number):
        super(RelativeWeek, self).__init__(
            expression, calc_number, convert_type='week'
        )


class RelativeMonth(RelativeFunc):
    """Coerce an expression to a new field type."""

    def __init__(self, expression, calc_number):
        super(RelativeMonth, self).__init__(
            expression, calc_number, convert_type='month'
        )


class RelativeYear(RelativeFunc):
    """Coerce an expression to a new field type."""

    def __init__(self, expression, calc_number):
        super(RelativeYear, self).__init__(
            expression, calc_number, convert_type='year'
        )


class RelativeHour(RelativeFunc):
    """Coerce an expression to a new field type."""

    def __init__(self, expression, calc_number):
        super(RelativeHour, self).__init__(
            expression, calc_number, convert_type='hour'
        )


class RelativeMinute(RelativeFunc):
    """Coerce an expression to a new field type."""

    def __init__(self, expression, calc_number):
        super(RelativeMinute, self).__init__(
            expression, calc_number, convert_type='minute'
        )


class RelativeSecond(RelativeFunc):
    """Coerce an expression to a new field type."""

    def __init__(self, expression, calc_number):
        super(RelativeSecond, self).__init__(
            expression, calc_number, convert_type='second'
        )


class Epoch(Func):
    template = 'EXTRACT(epoch FROM %(expressions)s)::INTEGER'
    output_field = IntegerField()
