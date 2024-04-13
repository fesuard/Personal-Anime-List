from django import forms
from animeList.models import Anime


class AddAnimeForm(forms.ModelForm):
    class Meta:
        model = Anime
        fields = '__all__'


class UpdateAnimeForm(forms.ModelForm):
    class Meta:
        model = Anime
        fields = '__all__'

