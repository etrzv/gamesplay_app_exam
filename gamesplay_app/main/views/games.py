from django.shortcuts import render, redirect
from gamesplay_app.main.forms import CreateGameForm, EditGameForm, DeleteGameForm
from gamesplay_app.main.models import Game


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


def details_game(request, pk):
    game = Game.objects.get(pk=pk)
    context = {'game': game}
    return render(request, 'details-game.html', context)


def edit_game(request, pk):
    game = Game.objects.get(pk=pk)

    if request.method == 'GET':
        # TODO ! ! !
        form = EditGameForm(request.GET, instance=game)
        context = {
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
                'form': form
            }
            return render(request, 'edit-game.html', context)


def delete_game(request, pk):
    game = Game.objects.get(pk=pk)
    if request.method == 'POST':
        game.delete()
        return redirect('show dashboard')

    form = DeleteGameForm(instance=game)
    context = {'form': form}
    return render(request, 'delete-game.html', context)

    # game = Game.objects.get(pk=pk)
    #
    # if request.method == 'POST':
    #     form = DeleteGameForm(request.POST, instance=game)
    #
    #     if form.is_valid():
    #         form.save()     # / delete()
    #         return redirect('show dashboard')
    #
    # else:
    #     form = DeleteGameForm(instance=game)
    #
    # context = {
    #     'form': form,
    #     'game': game
    # }
    # return render(request, 'delete-game.html', context)

#     game = models.GameModel.objects.get(id=game_id)
#     if request.method == 'POST':
#         game.delete()
#         return redirect('dashboard-page')
#
#     form = forms.DeleteGameForm(instance=game)
#     context = {'form': form}
#     return render(request, 'delete-game.html', context)

# def delete_expense(request, pk):
#     expense = Expense.objects.get(pk=pk)
#
#     if request.method == 'POST':
#         form = DeleteExpenseForm(request.POST, instance=expense)
#         if form.is_valid():
#             form.save()
#             return redirect('show index')
#     else:
#         form = DeleteExpenseForm(instance=expense)
#
#     context = {
#         'form': form,
#         'expense': expense
#     }
#     return render(request, 'expense-delete.html', context)
