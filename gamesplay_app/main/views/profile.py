from django.shortcuts import render, redirect

from gamesplay_app.main import models
from gamesplay_app.main.forms import CreateProfileForm, EditProfileForm


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
        # 'no_profile': True

    }
    return render(request, 'create-profile.html', context)


def details_profile(request):
    form = EditProfileForm(request.POST)

    context = {
        'form': form,
    }

    return render(request, 'details-profile.html', context)


def edit_profile(request):
    return render(request, 'edit-profile.html')


def delete_profile(request):
    profile = models.Profile.objects.first()
    games = models.Game.objects.all()

    if request.method == 'POST':
        profile.delete()
        games.delete()
        return redirect('show index')

    return render(request, 'delete-profile.html')

