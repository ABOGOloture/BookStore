from django.urls import path
from . import views

urlpatterns = [
    path('book', views.BookList.as_view()),
    path('book/<int:pk>', views.BookDetails.as_view()),
]