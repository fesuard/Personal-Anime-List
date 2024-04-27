from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView, ListView, DetailView
from animeList.models import Anime, Tag, UserAnime
from animeList.forms import AddAnimeForm, UpdateAnimeForm, UserAnimeForm, UserAnimeUpdateForm
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
    all_grades = UserAnime.objects
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
    template_name = 'animeList/anime_search_list.html'
    model = Anime
    context_object_name = 'all_anime'

    def get_queryset(self):
        return Anime.objects.exclude(picture__isnull=True).exclude(picture='')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        # ce scriem in bara de search din navbar o sa fie si ca title in cea de advanced search
        q = self.request.GET.get('anime_title', '')
        adv_search_anime = Anime.objects.exclude(picture__isnull=True).exclude(picture='').exclude(
            picture='https://raw.githubusercontent.com/manami-project/anime-offline-database/master/pics/no_pic.png')
        myFilter = AnimeFilter(self.request.GET, queryset=adv_search_anime)
        adv_search_anime = myFilter.qs
        data['all_anime'] = adv_search_anime[:min(adv_search_anime.count(), 20)]
        data['filters'] = myFilter.form
        # data['simple_search_anime'] = simple_search_anime
        # randul de mai jos este ca sa ramana scris ce am cautat in bara de search, de asemenea in template a fost adaugat value="{{ q }}
        data['q'] = q
        return data


class AnimeDetailView(DetailView):
    model = Anime
    template_name = 'animeList/anime_detail_view.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        user_anime = UserAnime.objects.filter(anime=self.object, user=self.request.user).first()
        if user_anime is not None:
            form = UserAnimeForm(instance=user_anime)
        else:
            form = UserAnimeForm(initial={'anime': self.object})
        data['user_anime_form'] = form
        data['user_anime'] = user_anime
        return data


class CreateUserAnimeView(CreateView):
    model = UserAnime
    form_class = UserAnimeForm
    template_name = 'animeList/user_anime_create.html'

    # success_url = reverse_lazy('home-page')

    # def get_initial(self):
    #     return {'anime': self.request.GET.get('anime_id', Anime.objects.first().id)}

    def get_success_url(self):
        return self.request.META['HTTP_REFERER']

    def form_valid(self, form):
        if form.is_valid():
            user_anime = form.save(commit=False)
            user_anime.user = self.request.user
            user_anime.save()
            messages.success(self.request, 'Anime added to list!')
            return redirect(self.get_success_url())
        return super().form_valid(form)


class UpdateUserAnimeView(UpdateView):
    model = UserAnime
    form_class = UserAnimeForm
    template_name = 'animeList/user_anime_update.html'

    # success_url = reverse_lazy('home-page')

    def get_success_url(self):
        return self.request.META['HTTP_REFERER']


class AnimeUserListView(ListView):
    model = UserAnime
    template_name = 'animeList/anime_user_list_view.html'
    context_object_name = 'user_anime_list'

    def get_queryset(self):
        user = self.request.user
        return UserAnime.objects.filter(user=user.id)


class AnimeUserUpdateView(UpdateView):
    model = UserAnime
    template_name = 'animeList/user_anime_update_view.html'
    form_class = UserAnimeUpdateForm
    success_url = reverse_lazy('anime-list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # : UserAnime s-a folosit ca sa specificam clasa, ca sa iti faca autofill (ex linia 149)
        user_anime: UserAnime = self.object
        form.fields['eps_seen'].widget.attrs.update(
            {'class': 'form-control', 'min': '0', 'max': f'{user_anime.anime.episodes}'})
        return form


def stats_view(request):
    user = request.user
    scores = {}
    for i in range(1, 11):
        scores_grade = UserAnime.objects.filter(user=user, score=i).count()
        scores.update({f'{i}': scores_grade})
    tags = UserAnime.objects.filter(user=user).values('anime__tags')
    statuses = UserAnime.objects.filter(user=user).values('watch_status')
    context = {
        'scores': scores,
        'tags': tags,
        'statuses': statuses,
    }

    return render(request, 'animeList/stats.html', context)
