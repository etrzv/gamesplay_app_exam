from django.shortcuts import render


def create_game(request):
    return render(request, 'create-game.html')


def details_game(request):
    return render(request, 'details-game.html')


def edit_game(request):
    return render(request, 'edit-game.html')


def delete_game(request):
    return render(request, 'delete-game.html')
