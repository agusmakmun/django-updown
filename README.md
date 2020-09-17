# django-updown-ratings

> Simple Django application for adding Youtube like up and down voting. \
> This [`django-updown-ratings`][1] is forked from [`django-updown`][2] to support the newest django version.

[![Build Status](https://secure.travis-ci.org/agusmakmun/django-updown-ratings.png?branch=master)][3]

## Install

```
pip install django-updown-ratings
```

## Usage

Add `"updown"` to your `INSTALLED_APPS`. Then just add a `RatingField` to your existing model:

```
from django.db import models
from updown.fields import RatingField

class Post(models.Model):
    # ...other fields...
    rating = RatingField()
```

You can also allow the user to change his vote:

```
class Post(models.Model):
    # ...other fields...
    rating = RatingField(can_change_vote=True)
```

Now you can write your own view to submit ratings or use the predefined:

```
from updown.views import AddRatingFromModel

urlpatterns = [
  ...
  path('<int:object_id>/rate/<str:score>', AddRatingFromModel(), {
      'app_label': 'post',
      'model': 'Post',
      'field_name': 'rating'
  }, name='post_rating'),
]
```

To submit a vote just go to ``post/<id>/rate/(1|-1)``. If you allowed users to
change they're vote, they can do it with the same url.


[1]: https://github.com/agusmakmun/django-updown-ratings
[2]: https://github.com/weluse/django-updown
[3]: http://travis-ci.org/agusmakmun/django-updown-ratings
