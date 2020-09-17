# django-updown-ratings

> Simple Django application for adding Youtube like up and down voting. \
> This [`django-updown-ratings`][1] is forked from [`django-updown`][2] to support the newest django version.

[![build status][3]][4]
[![django version][5]][6]
[![python version][7]][8]

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
    ....

    path('<int:object_id>/rate/<str:score>', AddRatingFromModel(), {
        'app_label': 'blogapp',
        'model': 'Post',
        'field_name': 'rating'
    }, name='post_rating'),
]
```

To submit a vote just go to `post/<id>/rate/(1|-1)`. If you allowed users to
change they're vote, they can do it with the same url.

#### Template

You can directly use this properties in the template, e.g:

```
{{ post.rating.likes }}
{{ post.rating.dislikes }}
{{ post.rating.get_difference }}
{{ post.rating.get_quotient }}
```

**Properties:**

- `.likes` show total likes
- `.dislikes` show total dislikes
- `.get_difference` get diff between _likes_ and _dislikes_ (`likes - dislikes`).
- `.get_quotient` get quotient between _likes_ and _dislikes_ (`likes / max(dislikes)`).



[1]: https://github.com/agusmakmun/django-updown-ratings
[2]: https://github.com/weluse/django-updown

[3]: https://secure.travis-ci.org/agusmakmun/django-updown-ratings.png?branch=master
[4]: http://travis-ci.org/agusmakmun/django-updown-ratings

[5]: https://img.shields.io/badge/Django-2.0%20%3E=%203.1-green.svg
[6]: https://www.djangoproject.com

[7]: https://img.shields.io/pypi/pyversions/django-updown-ratings.svg
[8]: https://pypi.python.org/pypi/django-updown-ratings
