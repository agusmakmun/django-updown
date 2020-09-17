from django.db import models
from updown.fields import RatingField


class Post(models.Model):
    title = models.CharField(max_length=200)
    rating = RatingField(can_change_vote=True)

    def __str__(self):
        return self.title
