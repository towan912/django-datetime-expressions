from django.db import models


class Article(models.Model):
    date = models.DateTimeField(null=True)
