import math

from django.shortcuts import render, redirect
from gamesplay_app.main import models


def show_home(request):
    profile = models.Profile.objects.first()
    context = {
        'profile': profile,
    }

    return render(request, 'home-page.html', context)


def show_dashboard(request):
    profile = models.Profile.objects.first()
    games = models.Game.objects.all()
    all_ratings = []

    for game in games:
        ceil_stars = math.ceil(game.rating)
        all_ratings.append(ceil_stars)

    context = {
        'profile': profile,
        'games': games,
        'all_ratings': all_ratings,
    }
    return render(request, 'dashboard.html', context)
