from django.urls import path
from animeList import views

urlpatterns = [
    path('create_anime/', views.AnimeCreateView.as_view(), name='create-anime'),
    path('update_anime/', views.AnimeUpdateView.as_view(), name='update-anime'),
]