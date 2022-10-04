from django.shortcuts import render, redirect

from gamesplay_app.main.models import Profile


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def show_home(request):
    profile = get_profile()

    if not profile:
        return redirect('show dashboard')

    return render(request, 'home-page.html')


def show_dashboard(request):
    return render(request, 'dashboard.html')



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
