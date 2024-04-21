import django_filters
from django import forms
from animeList.models import Anime


class AnimeFilter(django_filters.FilterSet):
    type_choice = [
        ('SPECIAL', 'special'),
        ('TV', 'tv'),
        ('MOVIE', 'movie'),
        ('OVA', 'ova'),
        ('ONA', 'ona'),
        ('UNKNOWN', 'unknown'),
    ]
    status_choice = STATUS = [
        ('ONGOING', 'ongoing'),
        ('FINISHED', 'finished'),
        ('UPCOMING', 'upcoming'),
        ('UNKNOWN', 'unknown'),
    ]
    season_choice = [
        ('SPRING', 'spring'),
        ('SUMMER', 'summer'),
        ('WINTER', 'winter'),
        ('FALL', 'fall'),
    ]

    def filter_by_tags(self, queryset, value):
        # return queryset.filter(anime__tags__icontains=value)
        # return queryset.filter(tags__name__in=[value])
        return queryset.filter(tags__name__icontains=value)

    anime_title = django_filters.CharFilter(lookup_expr='icontains', field_name='title', label='Title', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Anime title'}))
    anime_status = django_filters.ChoiceFilter(widget=forms.RadioSelect(), field_name='status', choices=status_choice, label='Status')
    anime_type = django_filters.ChoiceFilter(widget=forms.RadioSelect(), field_name='type', choices=type_choice, label='Type')
    anime_year = django_filters.NumberFilter(label='Year', field_name='year', widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Anime year'}))
    anime_season = django_filters.ChoiceFilter(widget=forms.RadioSelect(), field_name='season', choices=season_choice, label='Season')
    anime_tags = django_filters.CharFilter(field_name='tags__name', lookup_expr='icontains', label='Tags', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Anime tags'}))

    class Meta:
        model = Anime
        fields = ['anime_title', 'anime_status', 'anime_type', 'anime_year', 'anime_season', 'anime_tags']
