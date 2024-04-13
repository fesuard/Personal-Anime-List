from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from animeList.models import Anime
from animeList.forms import AddAnimeForm, UpdateAnimeForm


class AnimeCreateView(CreateView):
    template_name = 'animeList/create_anime.html'
    model = Anime
    form_class = AddAnimeForm


class AnimeUpdateView(UpdateView):
    template_name = 'animeList/update_anime.html'
    model = Anime
    form_class = UpdateAnimeForm
