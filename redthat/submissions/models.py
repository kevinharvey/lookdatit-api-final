from django.db import models


class Submission(models.Model):
    title = models.CharField(max_length=200)
    external_link = models.URLField()
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
