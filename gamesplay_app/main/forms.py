from django import forms
from gamesplay_app.main.models import Game, Profile


class CreateProfileForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput
    )

    class Meta:
        model = Profile
        fields = ('email', 'age', 'password')


class CreateGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        # ('first_name', 'last_name', 'email', 'age', 'profile_picture')
