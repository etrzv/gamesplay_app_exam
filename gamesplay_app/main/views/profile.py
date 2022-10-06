from django.shortcuts import render, redirect
from gamesplay_app.main.forms import CreateProfileForm


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
        'no_profile': True

    }
    return render(request, 'create-profile.html', context)

# def create_profile(request):
#     if request.method == 'POST':
#         form = CreateProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('show index')
#     else:
#         form = CreateProfileForm()
#
#     # no_profile adds the 'Profile' button to the right side of the screen to all links except when you do not have a
#     # profile
#     context = {
#         'form': form,
#         'no_profile': True,
#     }
#
#     return render(request, 'home-no-profile.html', context)

def details_profile(request):
    return render(request, 'details-profile.html')


def edit_profile(request):
    return render(request, 'edit-profile.html')


def delete_profile(request):
    return render(request, 'delete-profile.html')
