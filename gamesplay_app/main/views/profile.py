from django.shortcuts import render


def create_profile(request):
    return render(request, 'create-profile.html')


def details_profile(request):
    return render(request, 'details-profile.html')


def edit_profile(request):
    return render(request, 'edit-profile.html')


def delete_profile(request):
    return render(request, 'delete-profile.html')
