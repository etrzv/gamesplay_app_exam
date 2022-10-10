from django.shortcuts import render, redirect
from gamesplay_app.main.forms import CreateGameForm


def create_game(request):
    if request.method == 'POST':
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show dashboard')
    else:
        form = CreateGameForm(request.POST)

    context = {
        'form': form,
    }

    return render(request, 'create-game.html', context)


def details_game(request):
    return render(request, 'details-game.html')


def edit_game(request):
    return render(request, 'edit-game.html')


def delete_game(request):
    return render(request, 'delete-game.html')
