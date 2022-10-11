from django.shortcuts import render, redirect

from gamesplay_app.main import models
from gamesplay_app.main.forms import CreateGameForm, EditGameForm, DeleteGameForm
from gamesplay_app.main.models import Game


def create_game(request):
    profile = models.Profile.objects.first()
    if request.method == 'POST':
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show dashboard')
    else:
        form = CreateGameForm(request.POST)

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'create-game.html', context)


def details_game(request, pk):
    profile = models.Profile.objects.first()
    game = Game.objects.get(pk=pk)
    context = {
        'profile': profile,
        'game': game
    }
    return render(request, 'details-game.html', context)


def edit_game(request, pk):
    profile = models.Profile.objects.first()
    game = Game.objects.get(pk=pk)

    if request.method == 'GET':
        # TODO ! ! !
        form = EditGameForm(initial=game.__dict__)
        context = {
            'profile': profile,
            'form': form,
        }
        return render(request, 'edit-game.html', context)
    else:
        form = EditGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('show dashboard')
        else:
            context = {
                'profile': profile,
                'form': form
            }
            return render(request, 'edit-game.html', context)


def delete_game(request, pk):
    profile = models.Profile.objects.first()
    game = Game.objects.get(pk=pk)

    if request.method == 'POST':
        game.delete()
        return redirect('show dashboard')

    form = DeleteGameForm(instance=game)

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'delete-game.html', context)
