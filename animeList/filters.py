import django_filters
from django import forms
from animeList.models import Anime, UserAnime


class AnimeFilter(django_filters.FilterSet):
    type_choice = [
        ("SPECIAL", "special"),
        ("TV", "tv"),
        ("MOVIE", "movie"),
        ("OVA", "ova"),
        ("ONA", "ona"),
        ("UNKNOWN", "unknown"),
    ]
    status_choice = STATUS = [
        ("ONGOING", "ongoing"),
        ("FINISHED", "finished"),
        ("UPCOMING", "upcoming"),
        ("UNKNOWN", "unknown"),
    ]
    season_choice = [
        ("SPRING", "spring"),
        ("SUMMER", "summer"),
        ("WINTER", "winter"),
        ("FALL", "fall"),
    ]

    # added function for the tags filter so that it won't return the same anime multiple times
    # as a lot of them have tags like "comedy" and "highschool comedy"
    def filter_for_search(self, queryset, name, value):
        queryset = queryset.filter(tags__name__icontains=value)
        return queryset.distinct()

    anime_title = django_filters.CharFilter(
        lookup_expr="icontains",
        field_name="title",
        label="Title",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Anime title"}),
    )
    anime_status = django_filters.ChoiceFilter(
        widget=forms.RadioSelect(), field_name="status", choices=status_choice, label="Status"
    )
    anime_type = django_filters.ChoiceFilter(
        widget=forms.RadioSelect(), field_name="type", choices=type_choice, label="Type"
    )
    anime_year = django_filters.NumberFilter(
        label="Year",
        field_name="year",
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Anime year"}),
    )
    anime_season = django_filters.ChoiceFilter(
        widget=forms.RadioSelect(), field_name="season", choices=season_choice, label="Season"
    )
    anime_tags = django_filters.CharFilter(
        method="filter_for_search",
        label="Tags",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Anime tags"}),
    )

    class Meta:
        model = Anime
        fields = ["anime_title", "anime_tags", "anime_status", "anime_type", "anime_year", "anime_season"]


class AnimeListFilter(django_filters.FilterSet):
    anime_type_choice = [
        ("SPECIAL", "special"),
        ("TV", "tv"),
        ("MOVIE", "movie"),
        ("OVA", "ova"),
        ("ONA", "ona"),
        ("UNKNOWN", "unknown"),
    ]
    anime_status_choice = [
        ("ONGOING", "ongoing"),
        ("FINISHED", "finished"),
        ("UPCOMING", "upcoming"),
        ("UNKNOWN", "unknown"),
    ]

    watch_status_choice = [
        ("watching", "Watching"),
        ("completed", "Completed"),
        ("on-hold", "On-hold"),
        ("dropped", "Dropped"),
        ("plan_to_watch", "Plan to Watch"),
    ]
    score_choice = [
        (1, "(1) Appalling"),
        (2, "(2) Horrible"),
        (3, "(3) Very Bad"),
        (4, "(4) Bad"),
        (5, "(5) Average"),
        (6, "(6) Fine"),
        (7, "(7) Good"),
        (8, "(8) Very Good"),
        (9, "(9) Great"),
        (10, "(10) Masterpiece"),
    ]

    # added function for the tags filter so that it won't return the same anime multiple times
    # as a lot of them have tags like "comedy" and "highschool comedy"
    def filter_for_tags(self, queryset, name, value):
        queryset = queryset.filter(anime__tags__name__icontains=value)
        return queryset.distinct()

    anime = django_filters.CharFilter(
        field_name="anime__title",
        lookup_expr="icontains",
        label="Title",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Anime title"}),
    )
    # tags = django_filters.CharFilter(field_name='anime__tags__name', lookup_expr='icontains', label='Tags', widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Anime tags'}))
    tags = django_filters.CharFilter(
        method="filter_for_tags",
        label="Tags",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Anime tags"}),
    )
    watch_status = django_filters.ChoiceFilter(
        widget=forms.RadioSelect(), choices=watch_status_choice, label="Watch Status"
    )
    score = django_filters.ChoiceFilter(widget=forms.RadioSelect(), choices=score_choice, label="Score")
    show_type = django_filters.ChoiceFilter(
        widget=forms.RadioSelect(), field_name="anime__type", label="Show Type", choices=anime_type_choice
    )

    class Meta:
        model = UserAnime
        fields = ["anime", "tags", "watch_status", "score", "show_type"]
