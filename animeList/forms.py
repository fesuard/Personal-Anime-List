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


class UserAnimeUpdateForm(forms.ModelForm):
    class Meta:
        model = UserAnime
        fields = ['score', 'eps_seen', 'watch_status']

    def __init__(self, *args, **kwargs):
        super(UserAnimeUpdateForm, self).__init__(*args, **kwargs)
        # self.fields['eps_seen'].widget.attrs.update({'class': 'form-control', 'min': '0', 'max': '7'})
        # print(*args)
        # print(dict(kwargs))
        # for k in kwargs.keys():
        #     print(str(kwargs.get(k)))
