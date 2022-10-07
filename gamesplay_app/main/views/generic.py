import math

from django.shortcuts import render, redirect
from gamesplay_app.main import models


# def get_profile():
#     profile = Profile.objects.all()
#     if profile:
#         return profile[0]
#     return None


def show_home(request):
    profile = models.Profile.objects.first()
    context = {
        'profile': profile,
    }

    # if not profile:
    #     return redirect('show dashboard')

    return render(request, 'home-page.html', context)


def show_dashboard(request):
    games = models.Game.objects.all()
    all_ratings = []

    for game in games:
        ceil_stars = math.ceil(game.rating)
        all_ratings.append(ceil_stars)

    context = {
        'games': games,
        'all_ratings': all_ratings,
    }
    return render(request, 'dashboard.html', context)


# def get_profile():
#     profile = Profile.objects.all()
#     if profile:
#         return profile[0]
#     return None
#
#
# def show_home(request):
#     profile = get_profile()
#
#     if not profile:
#         # redirects you to the url ! not the .html
#         return redirect('create profile')
#
#     expenses = Expense.objects.all()
#     budget_left = profile.budget - sum(e.price for e in expenses)
#
#     context = {
#         'profile': profile,
#         'expenses': expenses,
#         'budget_left': budget_left,
#     }
#     return render(request, 'home-with-profile.html', context)
