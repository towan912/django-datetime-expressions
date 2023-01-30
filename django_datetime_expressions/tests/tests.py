from typing import Union

from dateutil.relativedelta import relativedelta
from django.db.models import F
from django.test import TestCase
from django.utils import timezone

from django_datetime_expressions.expressions import (
    RelativeDay,
    RelativeHour,
    RelativeMinute,
    RelativeMonth,
    RelativeSecond,
    RelativeWeek,
    RelativeYear,
)
from django_datetime_expressions.tests.models import Article


class RelativeExpressionTestCaseBase(TestCase):
    expressions: Union[
        RelativeDay,
        RelativeHour,
        RelativeMinute,
        RelativeMonth,
        RelativeSecond,
        RelativeWeek,
        RelativeYear,
    ]

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        Article.objects.create(date=timezone.now())

    def test_addition(self):
        date_expression = self.expressions(F('date'), 1)

        article = Article.objects.annotate(
            additional_date=date_expression
        ).first()
        self.assertEqual(
            article.date + relativedelta(**{date_expression.convert_type: 1}),
            article.additional_date,
        )

    def test_subtraction(self):
        date_expression = self.expressions(F('date'), -1)

        article = Article.objects.annotate(
            additional_date=date_expression
        ).first()
        self.assertEqual(
            article.date - relativedelta(**{date_expression.convert_type: 1}),
            article.additional_date,
        )


class TestRelativeYear(RelativeExpressionTestCaseBase):
    expressions = RelativeYear


class TestRelativeMonth(RelativeExpressionTestCaseBase):
    expressions = RelativeMonth


class TestRelativeWeek(RelativeExpressionTestCaseBase):
    expressions = RelativeWeek


class TestRelativeDay(RelativeExpressionTestCaseBase):
    expressions = RelativeDay


class TestRelativeHour(RelativeExpressionTestCaseBase):
    expressions = RelativeHour


class TestRelativeMinute(RelativeExpressionTestCaseBase):
    expressions = RelativeMinute


class TestRelativeSecond(RelativeExpressionTestCaseBase):
    expressions = RelativeSecond
