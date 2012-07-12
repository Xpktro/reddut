from django.db import models
from redditApp import strings
from django.contrib.auth.models import User


# Create your models here.
class Link(models.Model):
    """Model class for a submitted Link"""

    verbose_name = strings.LINK

    link = models.URLField(
        verbose_name=strings.LINK_URL,
        blank=False,
    )

    description = models.CharField(
        verbose_name=strings.DESCRIPTION,
        max_length=200,
    )

    sub_date = models.DateTimeField(
        verbose_name=strings.SUB_DATE,
    )

    points = models.IntegerField(
        verbose_name=strings.POINTS,
    )

    sub_by = models.ForeignKey(User,
        verbose_name=strings.SUB_BY,
        null=True,
    )

    def __unicode__(self):
        return self.description

    class Meta:
        verbose_name = strings.LINK


class Comment(models.Model):
    """Model Class for an User Comment"""

    link = models.ForeignKey(
        Link,
        verbose_name=strings.LINK
    )

    comment = models.CharField(
        verbose_name=strings.COMMENT,
        max_length=1024,
        blank=False,
    )

    author = models.ForeignKey(
       User,
       verbose_name=strings.AUTHOR,
    )

    date = models.DateTimeField(
        verbose_name=strings.SUB_DATE,
    )

    points = models.IntegerField(
        verbose_name=strings.POINTS,
    )

    def __unicode__(self):
        return self.comment

    class Meta:
        verbose_name = strings.COMMENT
