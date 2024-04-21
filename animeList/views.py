from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, TemplateView, ListView
from animeList.models import Anime, Tag
from animeList.forms import AddAnimeForm, UpdateAnimeForm
from django.db import connection
from django.shortcuts import render
import random
from animeList.filters import AnimeFilter


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
    # tags = Tag.objects.filter(anime__in=random_anime)
    # anime_tags = []
    # for anime in random_anime:
    #     tags = Tag.objects.filter(anime__title=anime)
    #     anime_tags.append({anime: tags})
    context = {
        'random_anime': random_anime,
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


class AnimeSearchView(ListView):
    template_name = 'animeList/anime_list.html'
    model = Anime
    context_object_name = 'all_anime'

    def get_queryset(self):
        return Anime.objects.exclude(picture__isnull=True).exclude(picture='')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        q = self.request.GET.get('anime_title', '')
        adv_search_anime = Anime.objects.exclude(picture__isnull=True).exclude(picture='')
        # simple_search_anime = Anime.objects.filter(title__icontains=q)
        myFilter = AnimeFilter(self.request.GET, queryset=adv_search_anime)
        adv_search_anime = myFilter.qs
        data['all_anime'] = adv_search_anime[:min(adv_search_anime.count(), 20)]
        data['filters'] = myFilter.form
        # data['simple_search_anime'] = simple_search_anime
        # randul de mai jos este ca sa ramana scris ce am cautat in bara de search, de asemenea in template a fost adaugat value="{{ q }}
        data['q'] = q
        return data


# class AnimeAdvancedSearchView(ListView):
#     template_name = 'animeList/anime_list.html'
#     model = Anime
#     context_object_name = 'all_anime_adv'
#
#     def get_queryset(self):
#         return Anime.objects.all()
#
#     def get_context_data(self, **kwargs):
#         data = super().get_context_data(**kwargs)
#
#         animes = Anime.objects.all()
#         myFilter = AnimeFilter(self.request.GET, queryset=animes)
#         animes = myFilter.qs
#         data['all_anime_adv'] = animes
#         data['filters'] = myFilter.form
#
#         return data
