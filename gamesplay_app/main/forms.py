from django import forms
from gamesplay_app.main.models import Game, Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'
