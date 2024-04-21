from django.urls import path
from animeList import views

urlpatterns = [
    path('', views.home_view, name='home_page'),
    path('create_anime/', views.AnimeCreateView.as_view(), name='create-anime'),
    path('update_anime/', views.AnimeUpdateView.as_view(), name='update-anime'),
    path('seach_anime/', views.AnimeSearchView.as_view(), name='search-result'),

]