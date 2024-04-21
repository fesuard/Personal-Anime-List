from django import forms
from django.forms import TextInput, Select, NumberInput

from animeList.models import Anime
from animeList.models import UserAnime


class AddAnimeForm(forms.ModelForm):
    class Meta:
        model = Anime
        fields = '__all__'


class UpdateAnimeForm(forms.ModelForm):
    class Meta:
        model = Anime
        fields = '__all__'


class UserAnimeForm(forms.ModelForm):
    class Meta:
        model = UserAnime
        fields = ['watch_status', 'eps_seen', 'score', 'anime']

        widgets = {
            'anime': forms.HiddenInput(),
            'watch_status': Select(attrs={'class': 'form-select'}),
            'eps_seen': NumberInput(attrs={'class': 'form-control'}),
            'score': Select(attrs={'class': 'form-select'})
        }
