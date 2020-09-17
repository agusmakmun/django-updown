from django.urls import path
from updown.views import AddRatingFromModel

urlpatterns = [
    path('post/<int:object_id>/rate/<str:score>', AddRatingFromModel(), {
        'app_label': 'app',
        'model': 'Post',
        'field_name': 'rating'
    }, name='post_rating'),
]
