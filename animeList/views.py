from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, TemplateView, ListView
from animeList.models import Anime, Tag
from animeList.forms import AddAnimeForm, UpdateAnimeForm
from django.db import connection
from django.shortcuts import render
import random


def home_view(request):

    # Niste titluri din baza de data aveau caractere nesuportate, le-am sters cu codul comentat de mai jos
    # to_delete = []
    # for a in Anime.objects.all():
    #     try:
    #         print(a.id, a.title)
    #     except:
    #         to_delete.append(a)
    # for a in to_delete:
    #     print(f'Deleting {a.id}')
    #     a.delete()

    all_animes = Anime.objects.filter(tags__name__in=['family friendly', 'family life'])
    obj_to_select = 4
    random_anime = random.sample(list(all_animes), obj_to_select)
    random_tag = []
    for anime in random_anime:
        random_tag.append([Tag.objects.filter(anime__title=anime)])
    context = {
        'random_anime': random_anime,
        'random_tag': random_tag
    }
    return render(request, 'animeList/homepage.html', context)


class AnimeCreateView(CreateView):
    template_name = 'animeList/create_anime.html'
    model = Anime
    form_class = AddAnimeForm


class AnimeUpdateView(UpdateView):
    template_name = 'animeList/update_anime.html'
    model = Anime
    form_class = UpdateAnimeForm
