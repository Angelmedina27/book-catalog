from django.urls import path
from .views import BookListView, PublisherListView, ReviewListView

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('publishers/', PublisherListView.as_view(), name='publisher_list'),
    path('reviews/', ReviewListView.as_view(), name='review_list'),
]