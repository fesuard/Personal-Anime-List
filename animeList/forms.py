from django import forms
from django.core.exceptions import ValidationError
from django.forms import TextInput, Select, NumberInput

from animeList.models import Anime
from animeList.models import UserAnime
from django.contrib import messages


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

    def clean(self):
        cleaned_data = super().clean()
        watch_status = cleaned_data.get('watch_status')
        eps_seen = cleaned_data.get('eps_seen')
        anime = cleaned_data.get('anime')
        max_episodes = anime.episodes
        if watch_status == 'completed' and int(eps_seen) < int(max_episodes):
            raise ValidationError(f'Cannot be set as "completed" since you have seen {eps_seen}/{max_episodes} eps')
        if int(eps_seen) > int(max_episodes):
            raise ValidationError(f'Maximum number of episodes is: {max_episodes}')
        return cleaned_data


class UserAnimeUpdateForm(forms.ModelForm):
    # am specificat in init asta ca sa pot sa trimit self.request din form
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(UserAnimeUpdateForm, self).__init__(*args, **kwargs)

    class Meta:
        model = UserAnime
        fields = ['score', 'eps_seen', 'watch_status']

    # def __init__(self, *args, **kwargs):
    #     super(UserAnimeUpdateForm, self).__init__(*args, **kwargs)
    # self.fields['eps_seen'].widget.attrs.update({'class': 'form-control', 'min': '0', 'max': '7'})
    # print(*args)
    # print(dict(kwargs))
    # for k in kwargs.keys():
    #     print(str(kwargs.get(k)))

    def clean(self):
        cleaned_data = super().clean()
        watch_status = cleaned_data.get('watch_status')
        eps_seen = cleaned_data.get('eps_seen')
        anime = self.instance.anime
        max_episodes = anime.episodes
        if watch_status == 'completed' and int(eps_seen) < int(max_episodes):
            raise ValidationError(f'Cannot be set as "completed" since you have seen {eps_seen}/{max_episodes} eps')
        return cleaned_data
