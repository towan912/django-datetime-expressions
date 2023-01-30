from typing import Union

from dateutil.relativedelta import relativedelta
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


class _TestExpression(TestCase):
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
        super(_TestExpression, cls).setUpClass()
        Article.objects.create(date=timezone.now())

    def test_addition(self):
        article = Article.objects.annotate(
            additional_date=self.expressions(1)
        ).first()
        self.assertEqual(
            article.date + relativedelta(**{self.expressions.convert_type: 1}),
            article.additional_date,
        )

    def test_subtraction(self):
        article = Article.objects.annotate(
            additional_date=self.expressions(-1)
        ).first()
        self.assertEqual(
            article.date
            + relativedelta(**{self.expressions.convert_type: -1}),
            article.additional_date,
        )


class TestRelativeYear(_TestExpression):
    expressions = RelativeYear


class TestRelativeMonth(_TestExpression):
    expressions = RelativeMonth


class TestRelativeWeek(_TestExpression):
    expressions = RelativeWeek


class TestRelativeDay(_TestExpression):
    expressions = RelativeDay


class TestRelativeHour(_TestExpression):
    expressions = RelativeHour


class TestRelativeMinute(_TestExpression):
    expressions = RelativeMinute


class TestRelativeSecond(_TestExpression):
    expressions = RelativeSecond
