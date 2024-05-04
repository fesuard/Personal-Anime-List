from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView, TemplateView, ListView, DetailView
from animeList.models import Anime, Tag, UserAnime
from animeList.forms import UserAnimeForm, UserAnimeUpdateForm
from django.shortcuts import render
import random
from animeList.filters import AnimeFilter, AnimeListFilter


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

    all_animes = Anime.objects.filter(tags__name__in=['family friendly', 'family life']).exclude(picture='').exclude(
        picture='https://raw.githubusercontent.com/manami-project/anime-offline-database/master/pics/no_pic.png')
    obj_to_select = 4
    random_anime = random.sample(list(all_animes), obj_to_select)
    fact_list = [
        'Anime is a style of animation that originated in Japan and has become popular worldwide.',
        'The word "anime" is derived from the English word "animation."',
        'The first anime film ever made is "Momotaro, Sacred Sailors," released in 1945.',
        'Astro Boy, created by Osamu Tezuka in 1963, is considered one of the first successful anime series.',
        'Hayao Miyazaki is one of the most renowned anime directors, known for films like "Spirited Away" and "My Neighbor Totoro."',
        '"Dragon Ball Z" is one of the most popular and influential anime series worldwide.',
        '"Naruto" is another widely popular anime series, known for its compelling characters and epic battles.',
        '"One Piece" holds the Guinness World Record for the most copies published for the same comic book series by a single author.',
        '"Pokémon" is a globally recognized anime franchise, known for its video games, trading cards, and animated series.',
        '"Attack on Titan" is a dark fantasy anime series that has gained widespread acclaim for its intense action and compelling story.',
        'Studio Ghibli is a renowned Japanese animation studio responsible for many beloved anime films.',
        '"Death Note" is a psychological thriller anime series about a high school student who gains the power to kill anyone by writing their name in a notebook.',
        '"Fullmetal Alchemist" is a popular anime series known for its complex storyline and well-developed characters.',
        '"Sailor Moon" is a classic magical girl anime series that has inspired generations of fans.',
        '"Cowboy Bebop" is a critically acclaimed anime series that blends elements of science fiction, noir, and jazz music.',
        '"Neon Genesis Evangelion" is a groundbreaking mecha anime series known for its psychological themes and complex narrative.'
    ]
    random_fact = random.choice(fact_list)
    # The following block of code is for gettings some soft stats as in: the user's
    # avg score, no of animes in list, favorite tags
    if request.user.is_authenticated:
        user = request.user
        number_rated_anime = UserAnime.objects.filter(user=user).count()
        scores = UserAnime.objects.filter(user=user).values('score')
        score_list = []
        for score in scores:
            if score['score'] is not None:
                score_list.append(score['score'])
        if UserAnime.objects.filter(user=user).exists() and len(score_list) > 0:
            avg_score = sum(score_list) / len(score_list)
            animes_in_user_list = UserAnime.objects.filter(user=user).values('anime')
            tags = []
            tags_count = {}
            for anime in animes_in_user_list:
                anime_tags = Anime.objects.filter(id=anime['anime']).values_list('tags__name', flat=True)
                tags.extend(anime_tags)
            for tag in tags:
                tags_count[tag] = tags_count.get(tag, 0) + 1
            tags_count = sorted(tags_count.items(), key=lambda x: x[1], reverse=True)[:5]

            context = {
                'random_anime': random_anime,
                'random_fact': random_fact,
                'soft_stats': [number_rated_anime, avg_score, tags_count]
            }
            return render(request, 'animeList/homepage.html', context)
        else:
            no_message, no_stats = 'No anime rated yet', 0
            context = {
                'random_anime': random_anime,
                'random_fact': random_fact,
                'no_soft_stats': [no_message, no_stats]
            }
            return render(request, 'animeList/homepage.html', context)
    else:
        no_message, no_stats = 'Log in to create you list', 0
        context = {
            'random_anime': random_anime,
            'random_fact': random_fact,
            'no_soft_stats': [no_message, no_stats]
        }
        return render(request, 'animeList/homepage.html', context)


class AnimeSearchView(ListView):
    template_name = 'animeList/anime_search_list.html'
    model = Anime
    context_object_name = 'all_anime'

    def get_queryset(self):
        return Anime.objects.exclude(picture__isnull=True).exclude(picture='').exclude(
            picture='https://raw.githubusercontent.com/manami-project/anime-offline-database/master/pics/no_pic.png')

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
        messages.success(self.request, 'Anime updated successfully!')
        return self.request.META['HTTP_REFERER']


class AnimeUserListView(ListView):
    model = UserAnime
    template_name = 'animeList/anime_user_list_view.html'
    context_object_name = 'user_anime_list'

    def get_queryset(self):
        user = self.request.user
        return UserAnime.objects.filter(user=user.id)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        anime_in_list = UserAnime.objects.filter(user=self.request.user.id)
        myFilter = AnimeListFilter(self.request.GET, queryset=anime_in_list)
        anime_in_list = myFilter.qs
        data['user_anime_list'] = anime_in_list
        data['filters'] = myFilter.form
        return data


class AnimeUserUpdateView(UpdateView):
    model = UserAnime
    template_name = 'animeList/user_anime_update_view.html'
    form_class = UserAnimeUpdateForm

    # so that you can get self.request from form
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_success_url(self):
        messages.success(self.request, 'Anime updated successfully!')
        return self.request.META['HTTP_REFERER']

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        initial = super().get_initial()
        # : UserAnime s-a folosit ca sa specificam clasa, ca sa iti faca autofill (ex linia 149)
        user_anime: UserAnime = self.object
        form.fields['eps_seen'].widget.attrs.update(
            {'class': 'form-control', 'min': '0', 'max': f'{user_anime.anime.episodes}'})
        form.fields['score'].widget.attrs.update(
            {'class': 'form-control'})
        form.fields['watch_status'].widget.attrs.update(
            {'class': 'form-control'})
        return form


def stats_view(request):
    user = request.user
    scores = []
    for i in range(1, 11):
        scores_grade = UserAnime.objects.filter(user=user, score=i).count()
        scores.append((f'{i}', scores_grade))

    tags_count = {}
    tags = UserAnime.objects.filter(user=user).values_list('anime__tags__name', flat=True)
    for tag in tags:
        tags_count[tag] = tags_count.get(tag, 0) + 1
    tags_sorted = sorted(tags_count.items(), key=lambda x: x[1], reverse=True)[:min(len(tags_count), 15)]
    statuses = UserAnime.objects.filter(user=user).values_list('watch_status', flat=True)
    statuses_count = {}
    statuses_context = []
    for status in statuses:
        statuses_count[status] = statuses_count.get(status, 0) + 1
    for key, value in statuses_count.items():
        statuses_context.append((key, value))
    context = {
        'scores': scores,
        'tags': tags_sorted,
        'statuses': statuses_context,
    }

    return render(request, 'animeList/stats.html', context)
