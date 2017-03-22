from __future__ import unicode_literals
import re

from django.db import models

# Create your models here.
class ScoreManager(models.Manager):
    def validate(self,postData):
        errors = []
        if "initials" not in postData or "score" not in postData:
            errors.append("Incomplete data")
        else:
            if not re.search("^\w+$", postData["initials"]):
                errors.append("Letters only for name")
            if not re.search("^\d+$", postData["score"]):
                errors.append("Numbers only for score")
        if len(errors) == 0:
            newscore = Score.objects.create(initials=postData["initials"],score=postData["score"])
            return {"newscore":newscore}
        else:
            return {"errors":errors}


class Score(models.Model):
    initials = models.CharField(max_length=3)
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ScoreManager()
