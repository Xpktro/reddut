from django.db import models


# Create your models here.
class Link(models.Model):
    link = models.URLField()
    description = models.CharField(max_length=200)
    sub_date = models.DateTimeField("Date Submitted")
    points = models.IntegerField()
    #sub_by = models.CharField()

    def __unicode__(self):
        return self.description
