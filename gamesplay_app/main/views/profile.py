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
    profile = models.Profile.objects.first()
    all_games = models.Game.objects.all()
    total_games = len(all_games)
    avg_rating = 0

    if total_games > 0:
        avg_rating = sum(game.rating for game in all_games) / total_games
    else:
        avg_rating = 0.0

    context = {
        'profile': profile,
        'total_games': total_games,
        'avg_rating': avg_rating,
    }

    return render(request, 'details-profile.html', context)


def edit_profile(request):
    profile = models.Profile.objects.first()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = models.Profile.objects.first()
    games = models.Game.objects.all()

    if request.method == 'POST':
        profile.delete()
        games.delete()
        return redirect('show index')

    return render(request, 'delete-profile.html')


