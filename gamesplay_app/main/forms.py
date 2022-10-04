from django import forms
from gamesplay_app.main.models import Game


class CreateProfileForm(forms.ModelForm):
    pass


class CreateGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'
