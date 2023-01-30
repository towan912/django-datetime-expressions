from django.db.models.expressions import Func
from django.db.models.fields import DateTimeField, IntegerField


class RelativeFunc(Func):
    output_field = DateTimeField()
    template = (
        "%(expressions)s + CAST('%(value)i %(convert_type)s' as INTERVAL)"
    )

    def __init__(self, value, convert_type, output_field=None):
        super().__init__(output_field=output_field)
        self.value = value
        self.convert_type = convert_type


class RelativeDay(RelativeFunc):
    """Coerce an expression to a new field type."""

    def __init__(self, value):
        super().__init__(value, convert_type='day')


class RelativeWeek(RelativeFunc):
    """Coerce an expression to a new field type."""

    def __init__(self, value):
        super().__init__(value, convert_type='week')


class RelativeMonth(RelativeFunc):
    """Coerce an expression to a new field type."""

    def __init__(self, value):
        super().__init__(value, convert_type='month')


class RelativeYear(RelativeFunc):
    """Coerce an expression to a new field type."""

    def __init__(self, value):
        super().__init__(value, convert_type='year')


class RelativeHour(RelativeFunc):
    """Coerce an expression to a new field type."""

    def __init__(self, value):
        super().__init__(value, convert_type='hour')


class RelativeMinute(RelativeFunc):
    """Coerce an expression to a new field type."""

    def __init__(self, value):
        super().__init__(value, convert_type='minute')


class RelativeSecond(RelativeFunc):
    """Coerce an expression to a new field type."""

    def __init__(self, value):
        super().__init__(value, convert_type='second')


class Epoch(Func):
    template = 'EXTRACT(epoch FROM %(expressions)s)::INTEGER'
    output_field = IntegerField()
