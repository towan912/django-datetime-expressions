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


class __TestExpression(TestCase):
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
        super(__TestExpression, cls).setUpClass()
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


class TestRelativeYear(__TestExpression):
    expressions = RelativeYear


class TestRelativeMonth(__TestExpression):
    expressions = RelativeMonth


class TestRelativeWeek(__TestExpression):
    expressions = RelativeWeek


class TestRelativeDay(__TestExpression):
    expressions = RelativeDay


class TestRelativeHour(__TestExpression):
    expressions = RelativeHour


class TestRelativeMinute(__TestExpression):
    expressions = RelativeMinute


class TestRelativeSecond(__TestExpression):
    expressions = RelativeSecond
